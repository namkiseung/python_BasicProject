# -*- coding: utf-8 -*-


def find_and_count(target_string, string_to_find):
    """ 문자열 두개 target_string, string_to_find 를 전달 받아서, 
          target_string에 string_to_find가 몇개 포함되어 있는지 그 개수를 반환하는 함수를 작성하자
        
        sample data: target_string="Google", string_to_find="o"
        expected output: 2

        sample data: 'fizzbuzz', 'z'
        expected output: 4
    """
    # 여기 작성
    '''
    [행동]
    1. 인자 전달 받자
    2. 기준 문자열에 특정 문자열이 몇 개 포함되어있는지 알아보자

    문자열을 count함수로 매칭되는 숫자 구하기
    기준문자열.count(검색문자[,start[,end]])) -> int

    에러발생(원인은 기준문자열 타입이 튜플...)
        <class 'tuple'>
        <class 'str'>
        (해결방안)-> 문자열로 변환해서 중복되는 카운트값 찾자.       

    '''
    cd_target_string = str(target_string)
    num = cd_target_string.count(string_to_find)    
    return num


if __name__ == "__main__":
    target_string="Google",
    target_string2="""The biggest difference between a tuple and a list is worthless. The value of an item in a list is possible, and the value of an item in a tuple is not possible. Until then, you have to change the value without changing and always changing. Write the value on the McDonald's list. If the variable of the actual program value is used more than the average, it is used more."""
    target_string1='fizzbuzz'
    string_to_find="o"
    string_to_find1='z'

    '''
    양식
    - ('문자열 str', '찾을 char')
    - (중복횟수)
    
    '''
    print('기본문제<1>')
    print('sample data: target_string="Google", string_to_find="o"')
    print('expected output',find_and_count(target_string, string_to_find))
    print('')
    print('기본문제<1-1>')
    print('sample data: target_string="fizzbuzz", string_to_find="z"')
    print('expected output',find_and_count(target_string1, string_to_find1))
    print('')
    print('응용문제<2>')
    print('sample data: target_string2="Tupple and list difference...", string_to_find="o"')
    print('expected output',find_and_count(target_string2, string_to_find))
    #print
    pass

