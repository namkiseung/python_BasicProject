# -*- coding: utf-8 -*-



""" 정수 n을 전달받고, n의 factorial 을 반환하는 함수 factorial를 작성하자

    sample in/out:
        factorial(5) -> 120
        factorial(1) -> 1
        factorial(10) -> 3628800
"""
def factorial(num):
    num_sample=1
    for x in range(1, num+1):
        num_sample *= x
        
    return num_sample
if __name__ == "__main__":
    print(factorial(5))# -> 120
    print(factorial(1))# -> 1
    print(factorial(10))# -> 3628800
    pass
