# -*- coding: utf-8 -*-


def new_string(input_str):
    """ 문자열을 전달받고, 문자열의 앞에 "##" 를 붙여서 반환하는 함수를 작성하자
        단, 문자열에 "sh"가 포함되어 있으면, 전달받은 문자열을 그대로 반환한다
    
        sample in/out:
            new_string("stream") -> ##stream
            new_string("kakao") -> ##kakao
            new_string("ship") -> ship
    """
    if "sh" in input_str:
        return input_str
    return "##" + input_str


if __name__ == "__main__":
    print new_string("stream")# -> ##stream
    print new_string("kakao")# -> ##kakao
    print new_string("ship")# -> ship

