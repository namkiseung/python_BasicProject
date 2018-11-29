# -*- coding: utf-8 -*-


def replace_it(input_str):
    """ 입력된 문자열에 소문자 o를, 대문자 O로 바꿔서 반환하는 함수를 작성해보자
        hint: replace

        sample data: "google"
        expected output: "gOOgle"
    """
    result=input_str.replace('o', 'O')
    # 여기 작성
    return result

if __name__ == "__main__":
    input_str = 'google'
    print(replace_it(input_str))
    pass
