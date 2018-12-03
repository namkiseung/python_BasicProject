# -*- coding: utf-8 -*-


def new_string(input_str):
    """ 문자열을 전달받고, 문자열의 앞에 "##" 를 붙여서 반환하는 함수를 작성하자
        단, 문자열에 "sh"가 포함되어 있으면, 전달받은 문자열을 그대로 반환한다
    
        sample in/out:
            new_string("stream") -> ##stream
            new_string("kakao") -> ##kakao
            new_string("ship") -> ship
    """
    # 여기 작성
    #관건1 : 입력값에 ##을 붙혀준다
    #관건2 : 문자열 중에 'sh' 문자를 매칭해본다
        #관건2-2: 매칭되면 그대로 반환하고, 매칭 안되면 ##을 글자 앞에 붙혀준다
    for x in range(len(input_str)):
        if not input_str[x:x+2] == 'sh':
            result = '##'+input_str
            continue
        else:
            return input_str
    return result


if __name__ == "__main__":
    print new_string('stream')
    print new_string('kakao')
    print new_string('ship')
    print new_string('aisjdiajsidjiajsdjiaisdjiaewfbashaujsen iawegjaih')
    print new_string('ssaIdfjuasidgjaihgjairjgohajroigjaiorewgjo')
    pass

