# -*- coding:utf-8 -*-
#입력을 받자

"""
1번일 경우 add
2번일 경우 sub
3번일 경우 mul
4번일 경우 div
"""
import add, sub, mul, div

def thisadd(num1, num2):
    thisnum = num1 + num2
    return thisnum

def thissub(num1, num2):
    thisnum = num1 - num2
    return thisnum

def thismul(num1, num2):
    thisnum = num1 * num2
    return thisnum

def thisdiv(num1, num2):
    thisnum = num1 / num2
    return thisnum

if __name__ == "__main__":
    a = 10
    b = 10

#These num of import 
print 'result add :', add.add(a,b)  #add모듈의 함수
print 'result sub :', sub.sub(a,b)  #sub모듈의 함수  
print 'result mul :', mul.mul(a,b)  #mul모듈의 함수
print 'result div :', div.div(a,b)  #div모듈의 함수

#These thisnum of calc.py module
print 'this is result add :', thisadd(a,b)  #현재 모듈의 함수
print 'this is result sub :', thissub(a,b)  #현재 모듈의 함수  
print 'this is result mul :', thismul(a,b)  #현재 모듈의 함수
print 'this is result div :', thisdiv(a,b)  #현재 모듈의 함수

