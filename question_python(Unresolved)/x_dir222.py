# -*- coding: utf-8 -*-
import os, subprocess
import datetime
from os.path import join, getsize
""" cmd의 dir 역할을 하는 함수를 작성하자.
    os, datetime 모듈을 사용한다.
"""
workDir = os.path.abspath('.')  #전체 경
 #글자 '오후', '오전'
def files_output():
    #서브 프로세스 추가
    proc = subprocess.Popen(['vol'],
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = proc.communicate()
    print out
    
    ifafter_time_text = '오전'
    for dirpath, dirnames, filenames in os.walk(workDir):        
        #print (dirpath)
        #print ''
        for dirname in dirnames:                        
            ctime = os.path.getmtime(dirname) # 파일에 대한 시간(수정시간)
            lasttime=datetime.datetime.fromtimestamp(ctime) #출력 2018-07-25 17:36:52.935606

            trans_time=str(lasttime)[10:13] #datetime의 시간만 숫자로 변환
            if int(trans_time) >= 12:
                ifafter_time_text = '오후'
                
            print str(lasttime)[:10],ifafter_time_text+str(lasttime)[10:19],'  <DIR>',getsize(dirname), dirname
            
        for filename in filenames:
            ctime = os.path.getmtime(filename) # 파일에 대한 시간(수정시간)
            lasttime=datetime.datetime.fromtimestamp(ctime)

            trans_time=str(lasttime)[10:13] #datetime의 시간만 숫자로 변환
            if int(trans_time) >= 12:
                ifafter_time_text = ' 오후'
            print str(lasttime)[:10]+ifafter_time_text+str(lasttime)[10:19],'\t','', getsize(filename),filename
    return direct_size()

def getfoldersize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        #else:
        #elif os.path.isdir(itempath):
            #total_size += getfoldersize(itempath)
    return total_size

def direct_size():
    x=[]
    file_size=0 #파일 개수
    folder_size=0 #폴더 개수
    all_size=0
    a = os.stat('c:\\')    
    for root, dirs, files in os.walk(workDir):
        #print '##',sum([getsize(join(root, name)) for name in files]),'##'
        file_size += len(files)
        folder_size += len(dirs)
        #all_size+=sum([getsize(join(root, name)) for name in files])
        #print '총크기',all_size
    print '\t',str(file_size)+'개 파일','\t\t',a.st_size,' 바이트'
    print '\t',str(folder_size)+'개 디렉터리','\t\t',str_count_dat(a.st_mtime),'바이트 남음'    
    return ''
    
def str_count_dat(count_num): #긴 실수형에 콤마 넣기
    if count_num != 0:
        result = format(count_num, ',')            
    return result

def cmd_command_goods(command):
    return os.system(command)

def zero_plus(add_num): #한글자 일때 앞에 '0' 붙혀서 int로 반환
    a=''
    if len(str(add_num)) == 1:
        a=str(0)+str(add_num)     
        return a  
    return str(add_num)

def cmd_command_curio(command):
    #datetime.datetime.now() 
    d = datetime.date.today()
    
    return str(d.year)+'-'+zero_plus(d.month)+'-'+zero_plus(d.day)

def what_time_isit(filename):
    ctime = os.path.getctime(filename)
    
    return datetime.datetime.fromtimestamp(ctime)

'''
Q1. 숫자가 한글자 출력될때는 0 붙히기
Q2. 오전인지 오후인지 구분
Q3. 시간 붙히기
Q4. 디렉토리일 경우 <DIR> 붙히기
Q5. subprocess를 dir앞에 먼저 출력하고 시작하기

ex)
2018-07-09 오전 05:20 <DIR> [파일크기] [파일이름]
2018-07-09 오전 05:20 <DIR> [파일크기] [파일이름]
2018-07-09 오전 05:20 <DIR> [파일크기] [파일이름]

3개 파일 1,529 바이트
20개 디렉터리 54,371,332,096 바이트 남음
'''

if __name__=="__main__":
    #print cmd_command_goods("dir")            
    #print cmd_command_curio("dir")        
    #print getfoldersize("C:/Users/student/Desktop")
    #print getfoldersize("E:")
    
    print files_output()
    print len(str(os.walk.files(workDir)))
    
