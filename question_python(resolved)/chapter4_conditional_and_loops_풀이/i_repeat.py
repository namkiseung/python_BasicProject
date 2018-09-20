# -*- coding: utf-8 -*-


def repeat(msg, cnt):
    """ 문자열 과 정수(positive)를 전달받고, 문자열을 정수만큼 반복한 문자열을 만들어 반환하는 함수를 작성하자

        sample in/out:
            repeat("Hello", 1) -> "Hello"
            repeat("Hello", 3) -> "HelloHelloHello"
            repeat("Ha", 2) -> "HaHa"
    """
##    r = ""
##    for i in range(cnt):
##        r += msg   #  r = r + msg
    r = msg * cnt
    return r


if __name__ == "__main__":
    print repeat("Hello", 1)# -> "Hello"
    print repeat("Hello", 3)# -> "HelloHelloHello"
    print repeat("Ha", 2)# -> "HaHa"

