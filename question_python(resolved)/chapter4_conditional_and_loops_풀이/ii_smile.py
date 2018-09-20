# -*- coding: utf-8 -*-


def smile(input_str):
    """ 문자열을 전달받아서, 문자열 내에 ee가 있으면, ee를 :) 로 치환해서 반환하는 함수를 작성하자
        (ee가 없으면 그대로 반환한다)
    
        sample in/out:
            smile("sleep") -> "sl:)p"
            smile("weekend") -> "w:)kend"
    """
    r = input_str.replace("ee", ":)")
    return r


if __name__ == "__main__":
    print smile("sleep")# -> "sl:)p"
    print smile("weekend")# -> "w:)kend"

