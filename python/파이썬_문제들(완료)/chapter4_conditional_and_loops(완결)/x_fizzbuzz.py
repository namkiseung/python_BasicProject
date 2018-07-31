# -*- coding: utf-8 -*-

def fizzbuzz(x):
    """ 양의 정수 x를 전달받고, 1~x까지(경계 포함) 의 수를 리스트로 반환하는 함수를 작성한다
        단, 3의 배수는 "fizz", 5의 배수는 "buzz" 3과 5의 공배수는 "fizzbuzz"로 대체한다

        sample in/out:
            fizzbuzz(10) -> [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']
            fizzbuzz(20) -> [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']
    """
    # 여기 작성
    list_result = list()
    for result in range(1,x+1):
        
        if result%3==0:
            list_result.append('fizz')
        elif result%5==0:
            list_result.append('buzz')
        else:
            list_result.append(result)
    return list_result

if __name__ == "__main__":
    print fizzbuzz(5)
    print fizzbuzz(15)
    pass