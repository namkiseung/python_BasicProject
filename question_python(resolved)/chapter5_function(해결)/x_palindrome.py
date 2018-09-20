# -*- coding: utf-8 -*-



""" palindrome 여부를 True/False로 반환하는 함수 is_palindrome를 작성하자
    palindrome은 앞으로 읽으나 거꾸로 읽으나 똑같은 문자열을 의미한다

    sample in/out:
        is_palindrome('aza') -> True
        is_palindrome('azza') -> True
        is_palindrome('azba') -> False
"""

def is_palindrome(str_name):    
##    print(str_name[0:1], str_name[-1:])
##    print(str_name[0:2], str_name[-2:])
##    print(str_name[0:3], str_name[-3:])
##    print(':::',str_name[::1], str_name[::-1])
##    print(':::',str_name[::2], str_name[::-2])
##    print(':::',str_name[::3], str_name[::-3])
    
    
    return str_name[::-1]==str_name[::1]

if __name__ == "__main__": 
    print(is_palindrome('aza'))# -> True
    print(is_palindrome('azza'))# -> True
    print(is_palindrome('azba'))# -> False
    print(is_palindrome('aaaaaabaaaaa'))# -> False
    print(is_palindrome('aaaaabbbbb'))
    pass
