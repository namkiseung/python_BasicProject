# -*- coding: utf-8 -*-

err1 = """Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
""" # 이 에러가 나는 이유를 화면에 출력하자
print "#"*70
print err1
print u' 이 에러의 원인은? ', u'여기에 작성'  # <-
print "#"*70, "\n"


err2 = '''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError [Errno 2] No such file or directory: 'nonexistent.txt'
'''
print "#"*70
print err2
print u" 이 에러의 원인은?", u'여기에 작성'  # <-
print "#"*70, "\n"


code1 = """dict_a = {"key1": 100, "key2": 200, "key3": 300}
dict_a["key4"]
"""
print "#"*70
print code1
print u" 위 코드는 ", u" 여기에 작성", u" 에러를 발생시킨다"   # <-
print "#"*70, "\n"


# 아래 코드에서는 파일이 없으면, 에러가 발생할 수 있는데, 
# try except finally 구문을 이용해서 파일이 없으면! 파일을 만든 후
# default_data 의 내용을 파일에 입력한 후
# 나머지 처리(읽기, 화면에 출력하기)하도록 코드를 구성해보자.
def print_txt():
    default_data = "Hello world!"
    with open("none.txt", "r") as f:
        data = f.read()
        print data


# 정수를 입력받는 다음 함수를 완성시키자
# 정수가 아니면 예외가 발생하는데, 이를 적절히 처리하고
# 정상적으로 정수가 입력될때까지 반복한다
def get_int():
    while True:
        a = int(input("Input a number: "))
        break
    return a

