# -*- coding: utf-8 -*-

def fizzbuzz(x):
    """ 양의 정수 x를 전달받고, 1~x까지(경계 포함) 의 수를 리스트로 반환하는 함수를 작성한다
        단, 3의 배수는 "fizz", 5의 배수는 "buzz" 3과 5의 공배수는 "fizzbuzz"로 대체한다

        sample in/out:
            fizzbuzz(10) -> [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']
            fizzbuzz(20) -> [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']
    """
    r = []
    for i in range(1, x+1):
        if i%5==0 and i%3==0:
            r.append('fizzbuzz')
        elif i%3==0:
            r.append('fizz')
        elif i%5==0:
            r.append('buzz')
        else:
            r.append(i)
    return r

if __name__ == "__main__":
    print fizzbuzz(20)
