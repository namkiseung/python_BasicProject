# -*- coding: utf-8 -*-

##a = input('첫번째 숫자 입력 : ') 
##b = input('두번째 숫자 입력 : ')
##c = input('연산 기호 선택 : (1번 : 더하기)(2번 : 빼기)(3번 : 곱하기)(4번 : 나누기)')
import requests
def calculate(x,y,z):
    '''
    사용자 입력에 따라 다른 사칙연산을 하는
    하나의 함수를 가진 모듈을 작성
    '''
    result=0    
    if z == 1:
        result = x+y
    elif z == 2:
        result = x-y
    elif z == 3:
        result = x*y
    elif z == 4:
        result = x/y
    else:
        print "fail"
        
    return result

if __name__ == "__main__":    
    print calculate(a,b,c)    
    pass

