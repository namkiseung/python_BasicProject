# -*- coding: utf-8 -*-

name_book = [{'age': 31, 'fav': ['3g', 'chi', 'piz'], 'name': 'ttamna'},
            {'age': 32, 'fav': ['cof', 'greentea'], 'name': 'hope'}, 
            {'age': 22, 'fav': ['sprite', 'pepsi'], 'name': 'mirae'}, 
            {'age': 21, 'fav': ['choco', 'freetime'], 'name': 'gunin'}, 
            {'age': 2, 'fav': ['can', 'godunguh'], 'name': 'mango'}]
            
def get_firsts_type():
    """ name_book의 첫번째 요소의 타입을 반환하는 함수를 작성하자
    """
    # 여기 작성
    #1. name_book의 첫번째 요소들 출력
    #2. 요소를 타입으로 반환하기
    #3. format맞추어 반환    
    t_name1 = str(type(name_book[0]['fav']))
    t_name2 = str(type(name_book[0]['name']))
    t_name3 = str(type(name_book[0]['age']))
    
    #'age'
    #'fav'
    #'name'
    return print('1번 타입: '+t_name1+'\n2번 타입: '+t_name2+'\n3번 타입: '+t_name3)


if __name__ == "__main__":
    print(get_firsts_type())
    pass

