# -*- coding: utf-8 -*-

def fibonacci(end):
    """ 양의 정수 x를 입력받고, x 까지의 피보나치 수열을 list로 반환하는 함수를 작성하자
        Note : The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
               Every next number is found by adding up the two numbers before it.

        sample in/out:
            fibonacci(20) -> [0, 1, 1, 2, 3, 5, 8, 13]
            fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
    """
    a = [0, 1]
    for i in range(end):
        x = a[-1] + a[-2]

        if x >= end:
            break
        
        a.append(x)
    return a

if __name__ == "__main__":
    print fibonacci(20)
