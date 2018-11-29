# -*- coding: utf-8 -*-


def insert_string(target, word):
    """ 문자열 두 개 target, word 를 전달받아서, word 를 target의 중간에 삽입해서 반환하는 함수를 작성하자.

        sample data: '[[]]', 'Python'
        expected output: "[[Python]]"

        sample data: '<<>>', 'HTML'
        expected output: "<<HTML>>"
    """
    #target
    #word    
    #target
    # 여기 작성
    result= word[:2]+target+word[2:]
    return result 


if __name__ == "__main__":
    sample_data ='Python'
    etc = '[[]]'

    sample_data2 = 'HTML'
    etc2 = '<<>>'
    print(insert_string(sample_data, etc))
    print(insert_string(sample_data2, etc2))
    pass

