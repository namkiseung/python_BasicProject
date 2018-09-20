# -*- coding: utf-8 -*-

import os
def where_am_i():
    """ 현재 실행되고 있는 스크립트가 있는 디렉토리 경로를 구해서 반환하는 함수를 작성하자
        hint: os.path.dirname
    """
    # 여기 작성
    
    return os.getcwd()


if __name__ == "__main__":
    print where_am_i()
    pass

