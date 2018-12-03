# -*- coding: utf-8 -*-


def get_only_first_and_last(input_list):
    """ list 를 전달받아서, 첫번째와 마지막 요소만 포함하는 list를 반환하는 함수를 작성해보자

        sample data: ["Red","Green","White" ,"Black"]
        expected output: ["Red", "Black"]
    """
    # 여기 작성
    result = list()  #list변수생성
    result = input_list[:1]   #첫번째 요소
    result += input_list[len(input_list)-1:] #마지막 요
    return result


if __name__ == "__main__":
    input_list = ["Red","Green","White" ,"Black"]
    print(get_only_first_and_last(input_list))
    pass
