# -*- coding: utf-8 -*-


def mask_first_character(input_string):
    """ 문자열 하나를 전달 받고, 첫번째 문자가 두번째 이후로 나오면,
        $로 치환하고 반환하는 함수를 작성하자

        sample data: "remarker"
        expected output: "rema$ke$"

        sample data: "aloha"
        expectec output: "aloh$"
    """
    # 여기 작성
    #첫번째 문자를 n이라고 하자
        #첫번째 문자를 구해라
        
    #첫번째 이후 n이 또 나오면 치환
    first_word = input_string[0]
    input_string=input_string.replace(first_word, '$',2)
    return first_word+input_string[1:]


if __name__ == "__main__":
    data = "remarker"
    print(mask_first_character(data))
    pass

