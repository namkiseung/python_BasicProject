# -*- coding: utf-8 -*-


def who_am_i():
    """ 현재 실행되고 있는 스크립트(이 스크립트)의 전체 경로를 반환하는 함수를 작성하자
        hint: __file__, os.path.realpath, os.path.abspath

        note: os.path.realpath는 (리눅스에서)symbolic link를 역참조해 원본 파일의 전체경로를 구해주는 반면,
              os.path.abspath는 명시한 파일의 정확한 전체경로를 구해준다
            >>> os.path.realpath('cel_symlink')
            '/home/i2sec/OnlineJudgeDeploy/data/backend/log/celery.log'

            >>> os.path.abspath('cel_symlink')
            '/home/i2sec/cel_symlink'
    """
    # 여기 작성
    return


if __name__ == "__main__":
    pass

