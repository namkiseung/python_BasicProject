# -*- coding: utf-8 -*-

import sys
def get_sys_args():
    """ 프로그램의 명령행 인자 목록을 반환하는 함수를 작성하자
        hint: sys.args
    """
    # sys.argv.append(1)
    # sys.argv.append(2)

   # for x in range(len(sys_str)):
    #   a +=sys.argv[x]
    #print type(sys.argv[0])
    return sys.argv[0:]


if __name__ == "__main__":
    print get_sys_args()
    pass

