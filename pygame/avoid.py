import pygame, time, random
'''
기본 
1. 파이게임 모듈 불러오기
2. 초기화 시킨다.
3. 이미지를 가져온다.
4. 계속 화면이 보이도록 한다.
    #####(반복문 시작)#######
   5. 화면을 깨끗하게 한다
   6. 모든 요소들을 다시 그린다
   7. 화면을 다시 그린다
   8. (종료조건시 ESC)게임 종료
www.pygame.org/docs/ref/time.html
ref : https://www.youtube.com/watch?v=EswYaZH4ZAQ
'''
#초기화 작업
pygame.init()
#디스플레이 크기
display_width=800
display_height=600
#폰트, 이미지 변수 선언
font_style="C:/Users/namki/Desktop/mosproject-master/Source/MineSweeper/Assets/ExternalPlugin/Effect/Shared/Fonts/Roboto-Thin.ttf"
p1="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\dude.png".replace('\\\\','/')
p2="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\badguy.png".replace('\\\\','/')
#디스플레이 모드
gameDisplay = pygame.display.set_mode((display_width, display_height))
#FPS
clock = pygame.time.Clock()
#이미지 로드
playerImg = pygame.image.load(p1)
attackerImg = pygame.image.load(p2)
#주인공 class선언
class Player(object):
    x=0
    y=0
    x_speed=0
    y_speed=0
    speed_bouns = 0
    width=40
    height=40
    
    def __init__(self, x, y): #이동좌표
        self.x=x
        self.y=y
    def update(self):  #공 속도 조절
        #방향키 누를때 위치 값
        if self.x_speed > 0:
            self.x_speed += self.speed_bouns
        elif self.x_speed < 0:
            self.x_speed -= self.speed_bouns

        if self.y_speed > 0:
            self.y_speed += self.speed_bouns
        elif self.y_speed < 0:
            self.y_speed -= self.speed_bouns
           
        self.x += self.x_speed# + self.speed_factor
        self.y += self.y_speed# + self.speed_factor        
        gameDisplay.blit(playerImg, (self.x, self.y))
    #전체적인 속도
    def left_bound(self):
        if self.x <=0:
            self.x_speed = self.x_speed * -1
    def right_bound(self):
        if self.x >= display_width - self.width:
            self.x_speed = self.x_speed * -1
    def top_bound(self):
        if self.y <=0:
            self.y_speed = self.y_speed * -1
    def bottom_bound(self):
        if self.y >=display_height - self.height:
            self.y_speed = self.y_speed * -1
    def bound(self):
        self.left_bound()
        self.right_bound()
        self.top_bound()
        self.bottom_bound()
    
    def rectangle(self): #플레이어랑 부딪히는 포인트
        return  pygame.Rect(self.x, self.y, self.width, self.height)
#방해물 클래스
class Attacker(object):
    x=0
    y=0
    x_speed=0
    y_speed=0
    width=40
    height=40
    has_reached_limit = False
    side=0
    
    def __init__(self):
        #총 4개의 keytype
        self.side = random.randint(1,4) #self.side =4   
        if self.side == 1: #왼쪽
            self.x = -60
            self.y = random.randint(0, display_height-self.height)
            self.x_speed = 10
        elif self.side == 2:#위
            self.x = random.randint(0, display_width-self.width)
            self.y=-60
            self.y_speed=10
        elif self.side == 3:#오른쪽
            self.x = display_width + 60
            self.y=random.randint(0, display_height-self.height)
            self.x_speed=-10
        elif self.side == 4:#아래
            self.x = random.randint(0, display_width-self.width)
            self.y=display_height+60
            self.y_speed=-10
    def update(self):
        self.x +=  self.x_speed
        self.y +=  self.y_speed
        gameDisplay.blit(attackerImg, (self.x, self.y))
        #떠다니는 공에 대한 산술식
        if self.side == 1 and self.x > display_width:
            self.has_reached_limit = True
        if self.side == 2 and self.y > display_height:
            self.has_reached_limit = True
        if self.side == 3 and self.x < -40:
            self.has_reached_limit = True
        if self.side == 4 and self.y < -40:
            self.has_reached_limit = True
        
    def rectangle(self): #닿는 좌표포인트
        return  pygame.Rect(self.x, self.y, self.width, self.height)
    
    def left_bound(self):
        if self.x <=0:
            self.x_speed = self.x_speed * -1
    def right_bound(self):
        if self.x >= display_width - self.width:
            self.x_speed = self.x_speed * -1
    def top_bound(self):
        if self.y <=0:
            self.y_speed = self.y_speed * -1
    def bottom_bound(self):
        if self.y >=display_height - self.height:
            self.y_speed = self.y_speed * -1
    def bound(self):
        self.left_bound()
        self.right_bound()
        self.top_bound()
        self.bottom_bound()
 
def game_loop(): #게임 무한 루프
    player = Player(display_width/2, display_height/2)
    attackers = []
    difficulty = 1.0
    score=0
    gameDisplay.fill((255,255,255))
    player.update() 
    pygame.display.update() 
    #gameDisplay.blit(playerImg, (player.x, player.y))
    alive = True
    while alive:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE)):
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.x_speed = 2
                if event.key == pygame.K_LEFT:
                    player.x_speed = -2
                if event.key == pygame.K_DOWN:
                    player.y_speed = 2
                if event.key == pygame.K_UP:
                    player.y_speed = -2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.x_speed = 0                                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.y_speed = 0
                
        gameDisplay.fill((255, 255, 255))
        player.bound()
        player.update()
        if len(attackers) < difficulty:
            attackers.append(Attacker())            
        ball_index = 0 #볼 기준점
        for ball in attackers: #볼을 계속해서 생성
            ball.update()  #볼을 다시 화면에 그리기
            if ball.rectangle().colliderect(player.rectangle()): #볼이랑 부딪혔을때
                death_screen(score) #게임끝
                
            if ball.has_reached_limit:   #볼 제한걸기             
                attackers.pop(ball_index ) #볼 하나씩 뺌
                ball_index -= 1
                player.speed_bouns += 0.01 
                score += 1  #점수
                difficulty += 0.1  #난이도
                #print("score : {},  difficulty: {}, player.speed_bouns : {}".format(score, difficulty,player.speed_bouns )
        pygame.display.update() #화면에 전체 다시 그리기 flip()도 가능
        clock.tick(160) #FPS
        
def main_screen():  #게임시작 전 첫 화면(스코어 화면)
    gameDisplay.fill((0, 0, 0))
    text = pygame.font.Font(font_style, 60)
    text_on_screen = text.render("공 피하기 게임 \n let's go \n (게임종료는 ESC)", True, (255, 255, 255))
    text_rect = text_on_screen.get_rect()
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_on_screen, text_rect)
    pygame.display.update()    
    time.sleep(2) #게임 시작 딜레이
    game_loop()
def death_screen(score):  #죽었을때 첫 화면(스코어 화면)
    gameDisplay.fill((0, 0, 0))
    text = pygame.font.Font(font_style, 60)
    msg="gameover !! \n score : {}".format(int(score))
    text_on_screen = text.render(msg, True, (255, 255, 255))
    text_rect = text_on_screen.get_rect()
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_on_screen, text_rect)
    pygame.display.update()
    time.sleep(2)
    main_screen()
    
main_screen()

