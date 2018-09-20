# -*- coding: utf-8 -*-


def pos_neg(n):
    """ 정수를 전달받고, 양수인지, 음수인지, 0인지를 반환하는 함수를 작성하자
          이 값 들 중 하나의 값을 문자열로 반환 -> positive/negative/zero
        
        sample in/out:
            pos_neg(10) -> "positive"
            pos_neg(-10) -> "negative"
            pos_neg(0) -> "zero"
    """
    # 여기 작성
    if n > 0:
        return 'positive'
    elif n < 0:
        return 'negative'
    else:
        return ' zero'
    


if __name__ == "__main__":
    print pos_neg(10) #-> "positive"
    print pos_neg(-10)#-> "negative"
    print pos_neg(0) #-> "zero"
    print pos_neg(-10)
    print pos_neg(0)
    print pos_neg(0)
    pass

