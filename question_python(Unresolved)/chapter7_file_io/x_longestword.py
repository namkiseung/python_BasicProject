# -*- coding: utf-8 -*-
import time

def longest_word(filename):
    """ 전달받은 파일에서 가장 긴 단어를 문자열로 반환하는 함수를 작성하자
    """
    with open(filename, 'r') as f:
        data = f.read().split()
    
    long_str = data[0]
    for x in data:
        print x
        if len(long_str) < len(x):
            time.sleep(0.1)
            long_str = x

    return long_str

if __name__ == "__main__":
    filename = "attachments/n_line_file.txt"
    print longest_word(filename)