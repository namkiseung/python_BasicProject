import pygame, time, random
#www.pygame.org/docs/ref/time.html
#ref : https://www.youtube.com/watch?v=EswYaZH4ZAQ
pygame.init()
display_width=800
display_height=600
font_style="C:/Users/namki/Desktop/mosproject-master/Source/MineSweeper/Assets/ExternalPlugin/Effect/Shared/Fonts/Roboto-Thin.ttf"
p1="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\dude.png".replace('\\\\','/')
p2="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\badguy.png".replace('\\\\','/')
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
playerImg = pygame.image.load(p1)
attackerImg = pygame.image.load(p2)
class Player(object):
    x=0
    y=0
    x_speed=0
    y_speed=0
    width=40
    height=40
    
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        gameDisplay.blit(playerImg, (self.x, self.y))
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
    def rectangle(self):
        return  pygame.Rect(self.x, self.y, self.width, self.height)
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
        self.side = random.randint(1,4)
        #self.side =4
        if self.side == 1: #왼쪽
            self.x = -60
            self.y = random.randint(0, display_height-self.height)
            self.x_speed = 10
        elif self.side == 2:#위
            self.x = random.randint(0, display_width-self.width)
            self.y=-60
            self.y_speed=10
        elif self.side == 3:#위
            self.x = display_width + 60
            self.y=random.randint(0, display_height-self.height)
            self.x_speed=-10
        elif self.side == 4:#위
            self.x = random.randint(0, display_width-self.width)
            self.y=display_height+60
            self.y_speed=-10
    def update(self):
        self.x +=  self.x_speed
        self.y +=  self.y_speed
        gameDisplay.blit(attackerImg, (self.x, self.y))
        #떠다니는 공에 대한 산
        if self.side == 1 and self.x > display_width:
            self.has_reached_limit = True
        if self.side == 2 and self.y > display_height:
            self.has_reached_limit = True
        if self.side == 3 and self.x < -40:
            self.has_reached_limit = True
        if self.side == 4 and self.y < -40:
            self.has_reached_limit = True
        
    def rectangle(self):
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

 
def game_loop():
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
            if event.type == pygame.QUIT:
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
            
        ball_index = 0
        for ball in attackers:
            ball.update()

            if ball.rectangle().colliderect(player.rectangle()):
                death_screen(score)
                
            if ball.has_reached_limit:                
                attackers.pop(ball_index )
                ball_index -= 1
                score += 1
                difficulty += 0.1
        pygame.display.update()
        clock.tick(160)
        
def main_screen():
    gameDisplay.fill((0, 0, 0))
    text = pygame.font.Font(font_style, 60)
    text_on_screen = text.render("let's go", True, (255, 255, 255))
    text_rect = text_on_screen.get_rect()
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_on_screen, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def death_screen(score):
    gameDisplay.fill((0, 0, 0))
    text = pygame.font.Font(font_style, 60)
    msg="gameover !! \n score : {}".format(score)
    text_on_screen = text.render(msg, True, (255, 255, 255))
    text_rect = text_on_screen.get_rect()
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_on_screen, text_rect)
    pygame.display.update()
    time.sleep(2)
    main_screen()
    
main_screen()
#7:38 https://www.youtube.com/watch?v=m9Y3ciEek-w&t=9s
