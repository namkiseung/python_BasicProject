# -*- coding: utf-8 -*-


def swap_last_first(input_list):
    """ 세개의 문자열을 요소로 갖는 list를 전달받아서, 첫번째와 세번째의 순서를 바꿔서 반환하는 함수를 작성해보자

        sample data: ["i2sec", "co", "kr"]
        expected output: ["kr", "co", "i2sec"]
    """
    # 여기 작성
    
    #첫번째를 임시에 넣고
    tmp = input_list[0]
    #첫번째 자리에 세번째 데이터 넣고
    input_list[0] = input_list[2]
    #세번째에 임시값
    input_list[2] = tmp
    return input_list


if __name__ == "__main__":
    sample_data = ["i2sec", "co", "kr"]
    print(swap_last_first(sample_data))
    pass
