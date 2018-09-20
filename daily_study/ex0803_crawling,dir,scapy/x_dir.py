# -*- coding: utf-8 -*-
import os
import datetime

def x_dir(path='.'):
    files = os.listdir(path)
    for f in files:
        #수정시간, 디렉토리인지 <dir> , 파일이면(크기), 파일이름
        #수정시간
                                            #datetime.datetime #날짜랑시간
                                            #datetime.time #시간
        timestamp = os.path.getmtime(f)
        dt = datetime.datetime.fromtimestamp(timestamp)
        tf = dt.strftime("%Y-%m-%d %p %H:%M") #참고 https://www.ibm.com/support/knowledgecenter/ko/ssw_ibm_i_73/rtref/strfti.htm

        #dir 여부
        d_isdir = os.path.isdir(f)

        # 크기(파일이면)
        if not d_isdir:
            size = os.path.getsize(f)

        #dirstr = "<DIR>" if d_isdir else ""
        if d_isdir:
            dirstr = "<DIR>"
            sizestr= " "
        else:
            dirstr = " "
            sizestr=str(size)

        print "{:20} {:<10} {:<10} {}".format(tf, dirstr, sizestr, f)    
        
        #파일크기는 psutil 모듈 이용하자
    pass


if __name__=="__main__":    
    print x_dir()