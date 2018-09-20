# -*- coding: utf-8 -*-

import os, glob
def listing2(path, ext):
    """ 디렉토리 경로 path와 파일 확장자 ext를 전달받아, 
          path 디렉토리에 있는 ext 확장자를 가진 파일만 반환하는 함수를 작성하자
        hint: glob, '*'
    """
    # 여기 작성
    
    # if os.path.isdir(path):
    #     return os.listdir(path)
    
    return glob.glob('{}\*{}'.format(path, ext))
    


if __name__ == "__main__":
    print listing2('C:\Users\student\Desktop', '.ext')
    print listing2('C:\Users\student\Desktop', '.exe')
    print listing2('C:\Users\student\Desktop', '.sh')
    pass

