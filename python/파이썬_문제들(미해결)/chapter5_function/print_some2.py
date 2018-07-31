# -*- coding: utf-8 -*-

v_global = 10
def print_some2(num):
    """ print_some1 은 실행시 에러가 발생하지 않는데, 이 함수는 에러가 발생한다
        에러의 이유에 대해 알아보고, 코드가 의도대로 동작하도록 주석을 해제하고 코드를 추가하자
    """
    #
    v_global += num            # 이 라인 코드 삭제 금지
    return v_global


if __name__ == "__main__":
    pass

