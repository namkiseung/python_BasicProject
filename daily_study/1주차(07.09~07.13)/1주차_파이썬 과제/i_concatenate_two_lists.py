# -*- coding: utf-8 -*-


def concatenate_two_lists(list1, list2):
    """ 두 개의 리스트를 전달받아서, 하나로 합쳐서 반환하는 함수를 작성해보자
        hint: extend 또는 +

        sample data: [10, 20, 30], [40, 50, 60]
        expected output : [40, 50, 60, 10, 20, 30]
    """
    # 여기 작성
    list3 = list1 + list2
    return list3


if __name__ == "__main__":
      sample_data = [10, 20, 30]    #첫번째 리스트
      sample_data2 = [40, 50, 60]    #두번째 리스트
         #expected_output = [40, 50, 60, 10, 20, 30] 
      a=concatenate_two_lists(sample_data, sample_data2)
      print(a)
    
    

