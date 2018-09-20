
""" cmd의 dir 역할을 하는 함수를 작성하자.
    os, datetime 모듈을 사용한다.
"""
import os, datetime
from os.path import join, getsize
##def search(dirname):
##    filenames = os.listdir(dirname)
##    for filename in filenames:
##        full_filename = os.path.join(filename)
##        print (full_filename)
##
##search("c:/")

workDIr = os.path.abspath('.')
for dirpath, dirnames, filenames in os.walk(workDIr):
    print (dirpath)

    for dirname in dirnames:
        print ("\t", dirname)

    for filename in filenames:
        print ("\t", filename)

#import os

for root, dirs, files in os.walk(workDIr):
    #print(root, "consumes", end="")
    print(sum([getsize(join(root, name)) for name in files]), end="")
    print("bytes in", len(files), "files")
    print("bytes in", len(dirs), "directories")
    print('낭믄값',os.stat('C:\\').count(self, 'C:\\'))
    
    #if 'CVS' in dirs:
    #    dirs.remove('CVS')  # don't visit CVS directories

    

#if __name__=="__main__":
 #   print(allfiles('namki'))
