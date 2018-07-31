# -*- coding: utf-8 -*-
import hashlib
import os

def get_n_line(filename, n):
    """ filename 변수로 전달받은 파일명을 이용해서 파일을 열어 읽고, 
        첫 n라인 만큼만 읽어서 리스트로 반환하는 함수를 작성하자

        sample in/out:
        get_n_line("attachments/n_line_file.txt", 3) 
          -> ["# List of the world's smartest animals\n", '1: Orangutan\n', '2: Bottlenose Dolphin\n']
    """
    a=[]
    with open(filename,'r') as f:
        data = f.readlines()        
        for x in data:
            a.append(x)

    return a[:n]

if __name__ == "__main__":        
    print get_n_line("attachments/n_line_file.txt", 3) 
    pass
