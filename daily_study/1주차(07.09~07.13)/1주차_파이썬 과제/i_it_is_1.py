# -*- coding: utf-8 -*-


def it_is_1():
    """ 아래 dict_a에서 favorite는 키인가? 값인가?
    """
    dict_a = {"year": 2017, "favorite": ["Chicken", "Pizza", "Zazangmyun", "Ramyun"], "phone": "01012345678"}

    a1 = u"키"
    a2 = u"값"
    nn = "I don't know~"

    #콜론 앞은 키(key) 뒤는 값(value)
    return a1   # nn을 답으로 대체


if __name__ == "__main__":
    print('정답은',"'",it_is_1(),"'")
    pass

