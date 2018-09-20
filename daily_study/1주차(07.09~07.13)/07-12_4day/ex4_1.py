# -*-coding:cp949 -*-
"""
>>> w = 'hello world'
>>> w[w.index('h')+1]
'e'
>>> w[6]
'w'
"""

str_default = 'i want to lol now'

"""
>>> print str_default[-1]
w
>>> print str_default[0:2]
i 
>>> print str_default[2:5]
wan
>>> print str_default[2:6]
want
>>> print str_default[7:9]
to
>>> print str_default[10:13]
lol
"""

"""
>>> print str_default.replace('i', 'I')  올드를 찾아서 뉴로 바꿔준다
I want to lol now
"""

#1. 문자열을 입력받아 'h'를 대문자 'H'로 바꿔 출력하기
input_str = 'we are hacker of i2sec academy'

def trans():
    result=input_str.replace('h', 'H')
    print result

trans()   #1번 문제의 답


#2. 문자열을 입력 받아 첫번째 공백(스페이스) 전까지만 출력하기
s = "Hello World"

#인덱싱이 글자가 공백이면 끝
for result2 in range(s.index('d')):
    if result2 == s.index(' '):
        print '공백의 위치는 ',result2,'번째 이며, 출력 결과는',s[:result2]        
    else:
        pass

#3. 문자 하나를 입력 받아 기존 문자열의 'e'를 입력 받은 문자로 바꿔 출력
s = "we are hacker"
c = 'a'

num3 = s.replace('e',c) #num3 = s.replace('e',raw_input())
print num3






