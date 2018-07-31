# -*- coding: utf-8 -*-


name_book = [{'age': 31, 'fav': ['3g', 'chi', 'piz'], 'name': 'ttamna'},
            {'age': 32, 'fav': ['cof', 'greentea'], 'name': 'hope'}, 
            {'age': 22, 'fav': ['sprite', 'pepsi'], 'name': 'mirae'}, 
            {'age': 21, 'fav': ['choco', 'freetime'], 'name': 'gunin'}, 
            {'age': 2, 'fav': ['can', 'godunguh'], 'name': 'mango'}]
            
def get_first():
    """ name_book의 첫번째 요소를 반환하는 함수를 작성하자
    """
    
    return name_book[0]


if __name__ == "__main__":
    print(get_first())
    pass

