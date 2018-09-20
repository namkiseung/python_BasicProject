# -*- coding: utf-8 -*-


def add_string(input_str):
    """ 문자열을 전달받아서 "ing"를 붙여서 반환하는 함수를 작성하자
        단, 입력받은 문자열의 끝 세자리가 "ing"면, "ly"를 붙여서 반환한다

        sample in/out:
            add_string("string") -> "stringly"
            add_string("str") -> "string"
            add_string("run") -> "runing"
    """
    # 여기 작성    
    if input_str[-3:]=='ing':
        result = input_str.replace('ing','ly')
        return result
    else:        
        return input_str+'ing'
    


if __name__ == "__main__":    
    print add_string("string")# -> "stringly"
    print add_string("str")# -> "string"
    print add_string("run")# -> "runing"
    pass

