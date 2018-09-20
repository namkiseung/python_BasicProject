# -*- coding:cp949 -*-
def list_str(a):
    words=a[:-1]
    words_cnt = len(a)
    return words, words_cnt



if __name__ == "__main__":
    a=[1,2,3,4,1,12,2,3,54,1,2,4]
    print list_str(a)
