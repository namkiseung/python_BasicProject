# -*- coding: utf-8 -*-


def square_dict(x):
    """ 
    1.     정수(positive) x를 전달받고 
    
    2.      1~x 까지(x포함)의 
            키를 가진 dict를 만들어서             
    
    3.      반환하는 함수를 작성하자
          
          
          (키의 쌍이 되는 값은 키의 제곱이다)        
        sample in/out:
            square_dict(10) -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
            square_dict(3) -> {1: 1, 2: 4, 3: 9}
    """
    # 여기 작성
    result=dict()
    xx=dict()
    
    for num in range(1,x+1):
        result.update({num:num*num})
        if len(result.keys()) == x:
            return result
    return "end"
    


if __name__ == "__main__":
    input_dict = 10
    input_dict2 = 3

    print square_dict(input_dict)
    print square_dict(square_dict2)
    
    pass

