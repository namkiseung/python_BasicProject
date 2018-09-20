# -*- coding : utf-8 -*-
# 3의 배수에 Fizz 5의 배수에 Bizz
# 둘다 해당하면 FizzBizz
# 나머진 그냥 숫자 0엔 ValueError

# 입력값은 1~100
def equal_num(num):
    a=""
    try:
        if num % 3==0 and num % 5==0:
            a = "FizzBizz"
        elif num % 5==0 or num % 3!=0:
            a = "Bizz"
        elif num % 5!=0 or num % 3==0:
            a = "Fizz"            
    except ValueError:
        a = "0"
        
    return a

if __name__=="__main__":
    for x in range(0, 100):
        print equal_num(x)
