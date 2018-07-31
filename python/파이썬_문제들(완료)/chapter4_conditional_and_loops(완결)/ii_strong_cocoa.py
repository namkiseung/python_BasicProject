# -*- coding: utf-8 -*-


def strong_cocoa(input_list):
    """ 리스트를 전달받고, 리스트 안에 "cocoa"가 있으면, "cocoa"를 대문자로 바꿔서 반환하는 함수를 작성하자
        
        sample in/out:
            s_list1 = ["apple", "banana", "cocoa", "durian"]
            s_list2 = ['sprite', 'pepsi']
            strong_cocoa(s_list1) -> ["apple", "banana", "COCOA", "durian"]
            strong_cocoa(s_list2) -> ['sprite', 'pepsi']
    """
    # 여기 작성
    #리스트 안에 'cocoa'가 있다면?(반복)
    for x in range(len(input_list)):        
        if input_list[x] == 'cocoa':            
            input_list[x] = input_list[x].upper()
            return input_list
        else:            
            continue

    return 'success'


if __name__ == "__main__":
    s_list1 = ["apple", "banana", "cocoa", "durian"]
    s_list2 = ['sprite', 'pepsi']

    print strong_cocoa(s_list1)
    print strong_cocoa(s_list2)
    pass

