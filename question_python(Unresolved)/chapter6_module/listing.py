# -*- coding: utf-8 -*-

import os
def listing(path):
    """ 디렉토리 경로를 전달받고, 디렉토리가 있으면, 그 디렉토리 아래 있는 것들의 목록을 반환하고,
        그런 디렉토리가 없으면 빈 리스트를 반환하는 함수를 작성하자
        hint: os.listdir, os.path.isdir
    """
    # 여기 작성
    b=[]
    if os.path.isdir(path):
        return os.listdir(path)
    
    return b


if __name__ == "__main__":
    print listing('C:\Users\student\Desktop')
    pass

