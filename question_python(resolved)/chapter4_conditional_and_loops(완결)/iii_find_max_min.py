# -*- coding: utf-8 -*-


def find_max_min(input_list):
    """ 전달받은 정수 리스트에서 가장 큰 값과, 가장 작은 값을 찾아 리스트형태로 반환하는 함수를 작성하자

    sample in/out:
        find_max_min([1,2,3,4,5]) -> [5, 1]
        find_max_min([-1,-2,-3,-4,-5]) -> [-1, -5]
    """
    #가장 큰값
    
    #가장 작은값
    min_num = input_list[0]
    max_num = input_list[0]
    for x in input_list:
        if x > max_num:
            max_num = x
        else:
            continue

    for y in input_list:
        if y < min_num:
            min_num = y
        else:
            continue

    
    
    # 여기 작성
    return max_num, min_num


if __name__ == "__main__":
    list_1 =[1,2,3,4,5]
    list_2 =[11,2,53,4,56,12,1,54,1,23,5,7,-4]
    list_3 =[-1,-2,-3,-4,-5]
    print find_max_min(list_1)
    print find_max_min(list_2)
    print find_max_min(list_3)
    pass

