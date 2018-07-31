# -*- coding: utf-8 -*-

import os
import time

def get_mtime(file_path):
    """ 파일이 마지막 수정된 시간을 반환하는 함수를 작성하자 (반환 형태: 'Wed Jan 10 14:21:58 2018' (문자열))
        hint: os.path.getmtime, time.ctime
        ctime(...)
            ctime(seconds) -> string
            Convert a time in seconds since the Epoch to a string in local time.
        getmtime(filename)
            Return the last modification time of a file, reported by os.stat().
    """
    
    #os.path()
    curdir=os.path.abspath('.')
    r=os.path.join(curdir, file_path)
    rr=os.path.getmtime(r) #수정시간 구하기
    return time.ctime(rr)


if __name__ == "__main__":
    print repr(get_mtime("C:\Users\student\Desktop\\namki_game.sh"))#찾을 파일의 절대경로
    #print repr(get_mtime("C:\Users\student\Desktop"))#찾을 디렉토리의 절대경로
    pass

