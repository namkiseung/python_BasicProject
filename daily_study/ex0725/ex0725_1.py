import os

#print dir(os)
#print os.getcwd() #getcwd 함수로 현재 경로를 얻을 수 있다는 것만 기억하기 바랍니다.
print os.listdir(os.getcwd())#특정 경로에 존재하는 파일과 디렉터리 목록을 구하는 함수(매개변수에는 경로를 넣어준다)

'''
해당 경로에 'exe'파일 확인하기
for x in os.listdir:
    if x.endswith('exe'):
        print x
'''

'''
import os, sys
#open file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
#Write one string
os.write(fd, "This is test")
#Close opend file
os.close()
'''
os.error()