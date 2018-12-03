# -*- coding: utf-8 -*-



""" 문자열을 전달 받아, 각 문자를 ascii ordinal value로 바꾼 목록을
반환하는 함수 get_ordinals를 작성하자

    sample in/out:
        get_ordinals("abcdefg") -> [97, 98, 99, 100, 101, 102, 103]
        get_ordinals("hello world") -> [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
"""
def get_ordinals(tu):
    #sam=list()
    a = tu.replace(' ','')
    print a
    #sam.append(chr(a))
    return #sam

if __name__ == "__main__":
    print get_ordinals("abcdefg") #-> [97, 98, 99, 100, 101, 102, 103]
    print get_ordinals("hello world") #->
    pass
