# -*- coding: utf-8 -*-


def add_string(input_str):
    """ 문자열을 전달받아서 "ing"를 붙여서 반환하는 함수를 작성하자
        단, 입력받은 문자열의 끝 세자리가 "ing"면, "ly"를 붙여서 반환한다
        sample in/out:
            add_string("string") -> "stringly"
            add_string("str") -> "string"
            add_string("run") -> "runing"
    """
    if input_str.endswith("ing"):
        r = input_str + "ly"
    else:
        r = input_str + "ing"
        
    return r


if __name__ == "__main__":
    print add_string("str")
    print add_string("run")
    print add_string("string")

