# -*- coding: utf-8 -*-


def reassembler(input_string):
    """ '-' 로 연결된 문자열을 전달받고, 
          '-'를 기준으로 쪼갠 후 정렬해서 
          다시 '-'로 이어붙여서 반환하는 함수를 작성하자
        hint: sort

        sample data: banana-cat-dinner-apple'
        expedted output: 'apple-banana-cat-dinner'
    """
    # 여기 작성
    result = input_string.split('-')
    result.sort()
    return result


if __name__ == "__main__":
    sample_data = 'banana-cat-dinner-apple'
    print(reassembler(sample_data))
    pass

