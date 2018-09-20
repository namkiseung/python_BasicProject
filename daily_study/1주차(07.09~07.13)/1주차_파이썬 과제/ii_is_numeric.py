# -*- coding: utf-8 -*-


def is_numeric(input_str):
    """ 문자열 하나를 전달받아서, 문자열이 숫자면 True를, 아니면 False 를 반환하는 함수를 작성하자

        sample data: "555"
        expected output: True

        sample data: "a55"
        expected output: False
    """
    #여기 작성
    
    if type(input_str) != type(' '):
        result = 'True'
    else:
        result = 'False'
    return result


if __name__ == "__main__":
    num1 = 555
    num2 = 'a55'
    print('1번 예제(입력값 : 555) : ',is_numeric(num1))
    print('2번 예제(입력값 : a55) : ',is_numeric(num2))
    
    pass

