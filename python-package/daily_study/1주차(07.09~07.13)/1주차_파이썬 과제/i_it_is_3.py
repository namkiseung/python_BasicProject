# -*- coding: utf-8 -*-


def it_is_3():
    """ 아래 dict_a에서 'year'를 참조해 얻을 수 있는 데이터의 타입은 무엇인가?
    """
    dict_a = {"year": 2017, "favorite": ["Chicken", "Pizza", "Zazangmyun", "Ramyun"], "phone": "01012345678"}
    a1 = "string"
    a2 = "list"
    a3 = "dictionary"
    a4 = "tuple"
    a5 = "integer"
    nn = "I don't know"
    return a5 # nn을 답으로 대체


if __name__ == "__main__":
   print('year을 참조해 얻는 데이터 타입은',it_is_3()) 
   pass

