# -*- coding: cp949 -*-

a=[1,2,3,'apple']
b={'aa':'apple', 'bb':'banana','cc':'c#','dd':'dictman'}
'''
1. list type 중 요소 초과로 뜨는 에러문자는 뭔가?  답: IndexError    
    ##print a[8]

    sample_result
    Traceback (most recent call last):
  File "E:/NamKi/python_class/python/ex0726/ex_except2.py", line 9, in <module>
    print a[8]
IndexError: list index out of range

########################################################################
2. list와 인덱스 번호를 인자로 받는 함수 get_element를 작성합니다.
    - 반환할 값은 list가 가진 요소 중, 인자로 받는 인덱스에 있는 요소
    - 인덱스 에러 발생시, 기본 값으로 None 반환
########################################################################    
3. dict 타입을 사용할 때, 존재하지 않는 키로 참조하려고 할 때 발생하는 에러가
무엇인지 확인합시다.

Traceback (most recent call last):
  File "E:/NamKi/python_class/python/ex0726/ex_except2.py", line 48, in <module>
    print get_element2(b, 'aaa')
  File "E:/NamKi/python_class/python/ex0726/ex_except2.py", line 41, in get_element2
    dicts[key_name] = key_name
NameError: global name 'dicts' is not defined

########################################################################
4. dict와 키를 인자로 받는 함수 get_value를 작성합니다
    - 반환할 값은 dict가 가진 요소 중, 인자로 받는 키와 매치되는 값
    - 키 에러 발생시, 기본 값으로 None 반환

'''


def get_element(listsss ,index_num):
    #comment='Index Error!!!!'    
    try:        
        print listsss[index_num]
    except IndexError:
        return None
    return listsss #list가 가진 요소 중, 인자로 받은 인덱스에 있는 요소 

def get_value(dictsss ,key_name):    
    try:        
        dicts[key_name] = ' '
    except NameError:
        return None
    return dicts 

if __name__=="__main__":
    print get_element(a, 2)
    print get_value(b, 'aaa')

'''
보너스 문제

import requests
res = requests.get(url)

5. 사용자로부터 입력 받은 웹 url의 페이지를 가져와 저장하는 프로그램을 만든다
    - 존재하지 않아 리퀘스트가 실패하면, 다시 입력하라는 메시지를 출력하고, 다시 입력 받음
    - 제대로 된 url을 입력 받았고, 파일 저장에 성공하면, 프로그램 종료
    
6. 모듈이 설치되어 있지 않아 ImportError가 발생할 때, 해당 모듈을 설치한 후 나머지 모드를 실행하도록, 예외처리를 작성해보자

'''
