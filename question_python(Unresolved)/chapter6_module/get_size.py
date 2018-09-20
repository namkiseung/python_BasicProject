# -*- coding: utf-8 -*-

import os
def get_size(file_path):
    """ 파일이름을 전달받아서 파일의 크기를 반환하는 함수를 작성하자
        hint: os.path.getsize
    """
    # 여기 작성
    r = os.path.getsize(file_path)
    s=r / 1024.0
    return "{} Kbyte".format(s)


if __name__ == "__main__":
    print (get_size("C:\Users\student\Desktop\\namki_game.sh"))#찾을 파일의 절대경로
    pass

