# -*- coding: utf-8 -*-

""" 양의 정수 x를 전달받아 그 수의 구구단을 반환하는 함수 get_gugu를 작성하자

    sample in/out:
        get_gugu(3) -> [3, 6, 9, 12, 15, 18, 21, 24, 27]
        get_gugu(8) -> [8, 16, 24, 32, 40, 48, 56, 64, 72]
"""
def get_gugu(x):
    a=list()
    for i in range(1, 10):        
        a.append(x*i)
        
    return a


if __name__ == "__main__":
    print get_gugu(8)
    pass

