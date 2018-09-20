# -*- coding: utf-8 -*-


def is_member(member_list, mem):
    """ 리스트 member_list 와, 어떤 데이터 mem을 전달받고, mem이 member_list에 포함되어 있는지를 True/False로 반환하는 함수를 작성하자

        sample in/out:
            is_member([1, 5, 8, 3], 3) -> True
            is_member([5, 8, 3], -1) -> False
    """
    # 여기 작성
    
    return mem in member_list
    
    


if __name__ == "__main__":
    print is_member([1, 5, 8, 3], 3)# -> True
    print is_member([5, 8, 3], -1) #-> False
    pass

