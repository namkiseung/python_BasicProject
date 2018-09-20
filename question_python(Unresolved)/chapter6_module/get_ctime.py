# -*- coding: utf-8 -*-
import os
import time


def get_ctime(file_path):
    """ 파일이 만들어진 시간을 반환하는 함수를 작성하자 
    (반환 형태: 'Wed Jan 10 14:21:58 2018' (문자열))
        hint: os.path.getctime, time.ctime
    """
    # 여기 작성
    
    #요일/월/일/시/분/초/연도
    filename = file_path
    curdir = os.path.abspath('.')
    abs_path = os.path.join(curdir, filename)
    all_result = os.path.getctime(abs_path) #파일의 생성일 알아냄
    end = time.ctime(all_result) #필터 거친 시간
    
    return end


if __name__ == "__main__":
    print repr(get_ctime("C:\Users\student\Desktop\\namki_game.sh"))#찾을 파일의 절대경로
    print repr(get_ctime("C:\Users\student\Desktop"))#찾을 디렉토리의 절대경로
    

    

