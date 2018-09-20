# -*- coding: utf-8 -*-


def monkey_trouble(a_smile, b_smile):
    """ 두 마리 원숭이가 있다. 두 마리 모두 웃고 있거나, 두 마리 모두 웃지 않으면 곤경에 빠집니다.
        a_smile, b_smile 각 원숭이가 웃는지/아닌지의 값을 가진다(True/False)
        두 값을 확인해서 위험하면 True를 반환하고, 그렇지 않으면 False를 반환하는 함수를 작성하자

        sample in/out:
            monkey_trouble(True, True) -> True
            monkey_trouble(False, False) -> True
            monkey_trouble(True, False) -> False
            monkey_trouble(False, True) -> False
    """
    # 여기 작성
    #xor이 이뤄질때 True 반환

    if a_smile==True and b_smile==True:
        return True
    elif a_smile==False and b_smile==False:        
        return True
    elif a_smile==True and b_smile==False:        
        return False
    else:
        return False
    
    return ''


if __name__ == "__main__":
    print monkey_trouble(True, True)# -> True
    print monkey_trouble(False, False) #-> True
    print monkey_trouble(True, False) #-> False
    print monkey_trouble(False, True) #-> False
    pass

