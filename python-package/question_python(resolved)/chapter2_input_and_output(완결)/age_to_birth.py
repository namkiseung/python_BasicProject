# -*- coding: utf-8 -*-

import sys
def age_to_birth(age):
    """ 나이를 인자로 입력받고, 출생년도를 화면에 출력하도록 해봅시다.
        hint: - 연산 사용
        !sample data: 23
        !output: 1995
    """

    now = 2018
    value = now-(age-1)
    print value, 'years'
    # 여기에 작성


if __name__ == "__main__":
    
    # 새로 작성, 주석 해제 등등 하면 됨(input 함수 사용)
    age = input('age? :')
    age_to_birth(age)

