# -*- coding:utf-8 -*-
import pygame as pg
from pygame.locals import *
import math
####
score = 0 # 점수 저장
playing = False #현재 게임이 플레이 중인지 확인하는 함수
####
#사용할 전역 변수 선언
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)

#초기화 | 초기화에 대한 stnout : (6, 0) 첫번째 6은 numpass이고, 0은 numfail이다) 
pg.init()


size=[750, 800]#GUI에 사용할 size변수
screen=pg.display.set_mode(size) #GUI 사이즈 설정
pg.display.set_caption("project") #GUI 타이틀 제목


done = False
clock=pg.time.Clock() #초당 화면 출력 변수(FPS)

def event_handler(): #game 종료 함수
    #for event in pg.event.get():
        
    pass
def event_exit():
    for event in pg.event.get(): #사용자 입력 이벤트 리스너
        if event.type == pg.QUIT: #종료 로직
            pass
            #done=True
            #pg.quit()
            #exit(0)

            
#이미지 로드
dog="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\dude.png".replace('\\\\','/')
player=pg.image.load(dog)
dog2="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\badguy.png".replace('\\\\','/')
player2=pg.image.load(dog2)
gameover="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\gameover.png".replace('\\\\','/')
youwin="C:\\Users\\namki\\Desktop\\hwang\\game-project\\resources\\images\\youwin.png".replace('\\\\','/')
#계속 화면 보이게

keys=[False,False,False,False]#플레이어 이동 변수
playerpos = [100,100]

'''
def win_losd_message():
    running=1
    if running:
        pg.font.init()
        font = pg.font.Font(None, 24)
        text = font.render("Accuracy :", True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(gameover, (0,0)) #출력
        screen.blit(text, textRect)
    else:
        pg.font.init()
        font = pg.font.Font(None, 24)
        text = font.render("Accuracy :", True, (0,255,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(youwin, (0,0)) #출력
        screen.blit(text, textRect)
    pass
'''
#메인 루프(while문)        
while not done:
    clock.tick(20) #루프 초당 10회로 제한
    pg.font.init()
    font = pg.font.Font(None, 24)
    text = font.render("Accuracy :", True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]    
    screen.blit(text, textRect)
    #화면설정
    screen.fill(WHITE) #(Surface클래스로 부터 가져옴)
    pg.display.update()    
    #플레이어 화면에 띄우기(이미지그리기)
    
    screen.blit(player2, (300,200)) #플레이어2
    #모든 요소 다시 그리기        
    
    for event in pg.event.get():
        if event.type == QUIT or (
             event.type == KEYDOWN and (
              event.key == K_ESCAPE or
              event.key == K_q
             )):
            pg.quit()
            quit()
            
        if event.type == pg.KEYDOWN:
            if event.key==pg.K_w:
                keys[0] = True #print("key w down")                
            elif event.key==pg.K_a:
                keys[1] = True
            elif event.key==pg.K_s:
                keys[2] = True #print("key s down")                
            elif event.key==pg.K_d:
                keys[3] = True
                
        if event.type == pg.KEYUP:
            if event.key==pg.K_w:
                keys[0] = False
            elif event.key==pg.K_a: #print("key a up")                
                keys[1] = False
            elif event.key==pg.K_s:
                keys[2] = False
            elif event.key==pg.K_d:
                keys[3] = False #print("key d up")
                
    #플레이어 움직임 포인터 로직
    if keys[0]:
        playerpos[1] = playerpos[1] - 5 #print("key :",playerpos)        
    elif keys[2]:
        playerpos[1] = playerpos[1] + 5 #print("key :",playerpos)        
    if keys[1]:
        playerpos[0] = playerpos[0] - 5 #print("key :",playerpos)        
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5 #print("key :",playerpos)        

    
    #플레이어 마우스 방향 포인터 설정
    position = pg.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26)) #회전 객체 생성
    playerrot = pg.transform.rotate(player, 360-angle*57.29) #회전객체의 마우스포인터 계산
    playerpos1 = (playerpos[0]-playerrot.get_rect().width//2, playerpos[1]-playerrot.get_rect().height//2) #get_tect이 사각형 포인터
    screen.blit(playerrot, playerpos1) #screen.blit((회전된 객체, 새로 만들어진 포지션)
    #event_handler() #ESC 종료 이벤트
    pg.display.flip() #화면 전체 업데이트(Surface클래스로 부터 가져옴)
#1. 파이게임 모듈 불러오기
#2. 초기화 시킨다.
#3. 이미지를 가져온다.
#4. 계속 화면이 보이도록 한다.
    #####(반복문 시작)#######
   #5. 화면을 깨끗하게 한다
   #6. 모든 요소들을 다시 그린다
   #7. 화면을 다시 그린다
   #8. (종료조건시)게임 종료
