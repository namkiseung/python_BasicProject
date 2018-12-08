import pygame
import turtle as t
import random

score = 0 # 점수 저장
playing = False #현재 게임이 플레이 중인지 확인하는 함수
te = t.Turtle()
#te.shape("turtle")
te.color("red")
te.speed(150)
te.up()
te.goto(0,200)

ts = t.Turtle()
#ts.shape("circle")
ts.color("green")
ts.speed(20)
ts.up()
ts.goto(0,-200)

def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)
def start(): #게임을 시작하는 함수
    global playing
    if playing ==False:
        playing =True
        t.clear() #메시지를 지움
        play()
def play():
    global score #
    global playing #
    t.fd(20) #w
    if random.randint(1,5) == 3: #1에서 5까지 임의수를 뽑는건데 임의수=3이면의 가정(20%확률)
        ang = te.towards(t.pos()) #position
        te.setheading(ang)
    speed = score + 25 #점수가 올라가면 빨라짐
    if speed > 115: #속도가 15를 넘지 않게함
        speed = 15
    te.forward(speed)
    if t.distance(te) < 12: #주인공과 거리가 12보다 작으면 게임을 종료함
        text = "Score:" +str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(ts) < 12: #주인공과 거리가 12보다 작으면
        score = score + 1 #점수를 올림
        t.write(score)#점수를 화면에 표시
        star_x = random.randint (-230, 230)
        star_y = random.randint (-230, 230)
        ts.goto(star_x, star_y) #먹이를 옮김
    if playing:
        t.ontimer(play, 100)

def message(m1,m2): #메세지를 화면에 표시
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run") #제목
t.setup(500,500)
t.bgcolor("orange")
#t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right") #방향키 오른쪽 화살표
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space") #시작
t.listen()
message("Turtle Run", "[space]") #첨가
