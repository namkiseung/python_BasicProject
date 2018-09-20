# -*- coding: utf-8 -*-


name_book = [{'age': 31, 'fav': ['3g', 'chi', 'piz'], 'name': 'ttamna'},
            {'age': 32, 'fav': ['cof', 'greentea'], 'name': 'hope'}, 
            {'age': 22, 'fav': ['sprite', 'pepsi'], 'name': 'mirae'}, 
            {'age': 21, 'fav': ['choco', 'freetime'], 'name': 'gunin'}, 
            {'age': 2, 'fav': ['can', 'godunguh'], 'name': 'mango'}]
            
def get_firsts_keys():
    """ name_book의 첫번째 요소의 키 목록을 반환하는 함수를 작성하자
    """
    first = name_book[0]
    # 여기 작성
    return first.keys()


if __name__ == "__main__":
    print(get_firsts_keys())
    pass

