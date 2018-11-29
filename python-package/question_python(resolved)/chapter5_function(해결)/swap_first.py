# -*- coding: utf-8 -*-



""" 문자열 하나를 전달받아,
첫 글자와 끝 글자를 서로 바꾼 후 반환하는 함수 swap_first를 작성하자

    sample in/out:
        swap_first("abcd") -> "dbca"
        swap_first("12345") -> "52341"
"""
def swap_first(str_ba):
    return str_ba[-1]+str_ba[1:-1]+str_ba[0]

if __name__ == "__main__":
    print(swap_first("abcd"))# -> "dbca"
    print(swap_first("12345"))# -> "52341"
    pass

