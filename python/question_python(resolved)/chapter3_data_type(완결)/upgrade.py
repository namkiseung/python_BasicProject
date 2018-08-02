#-*- coding:cp949 -*-

def change(num):
    '''
    문제
        실수 16자리 입력 받고
        4자리씩 끊어서 출력하기

    1234154150.00000000000000

    정수 출력 : 1234    1541   50
    소수 출력 : 0000  0000 0000 0000
    '''
    
    
   
    #숫자를 받고 길이를 재자
    strnum=repr(num)
    a=strnum.replace('.', '')
    
    #print(num.index('.'))
    return a[:4]+' '+a[4:8]+' '+a[8:12]+' '+a[12:16]#len(repr("%0.16f" % num))
    


if __name__ == "__main__":
    float_num1 = 514854875.0202002
    float_num2 = 158.1654168714554
    print(change(float_num1))
    print(change(float_num2))
