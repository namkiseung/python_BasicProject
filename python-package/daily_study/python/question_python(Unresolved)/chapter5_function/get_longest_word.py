# -*- coding: utf-8 -*-



""" 문자열 리스트를 전달받아, 가장 긴 문자열을 반환하는 함수 get_longest_word를 작성하자

    sample in/out:
        get_longest_word(['C', 'Web', 'python', 'linux']) -> 'python'
        get_longest_word(['google', 'apple', 'nokia', 'samsung']) -> 'samsung'
"""
def get_longest_word(list_t):
    list_t2=list_t
    word=list_t2[0]
    x=0
    for i in list_t:        
        if len(i) > len(word):
            word=i
            x=i
            #print len(word), word, len(i), i
        else:
            ""
            
    return x


if __name__ == "__main__":
    print get_longest_word(['C', 'Web', 'python', 'linux']) #-> 'python'
    print get_longest_word(['google', 'apple', 'nokia', 'samsung'])# -> 'samsung'
    pass

