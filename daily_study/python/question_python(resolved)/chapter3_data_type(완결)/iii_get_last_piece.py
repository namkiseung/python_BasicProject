# -*- coding: utf-8 -*-


def get_last_piece(target, delim):
    """ 문자열 두 개 target, delim 을 전달 받아서,
        target을 delim을 나눈 기준으로
        마지막 부분을 반환하는 함수를 작성하자

        sample data: "https://www.google.com", "."
        expected output: "com"

        sample data: "https://translate.google.com/#en/ko/split", "/"
        expected output: "split"
    """
    # 여기 작성
    
    
    return target.split(delim)[-1:]


if __name__ == "__main__":
    sample_data = "https://www.google.com"
    symbol = "."

    sample_data2 = "https://translate.google.com/#en/ko/split" 
    symbol2 = "/"
    print(get_last_piece(sample_data, symbol))
    print(get_last_piece(sample_data2, symbol2))
    pass


