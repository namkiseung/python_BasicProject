# -*- coding: utf-8 -*-

name_book = [{'age': 31, 'fav': ['3g', 'chi', 'piz'], 'name': 'ttamna'},
            {'age': 32, 'fav': ['cof', 'greentea'], 'name': 'hope'}, 
            {'age': 22, 'fav': ['sprite', 'pepsi'], 'name': 'mirae'}, 
            {'age': 21, 'fav': ['choco', 'freetime'], 'name': 'gunin'}, 
            {'age': 2, 'fav': ['can', 'godunguh'], 'name': 'mango'}]
            
def get_firsts_age():
    #get_firsts_age()는 첫번째 요소의 'age'의 키값을 반환하는 함수
    """ name_book의 첫번째 요소는 dict인데, 
          이 dict에서 키 'age'를 참조해 그 값을 반환하는 함수를 작성하자
    """
    # 여기 작성    
    return name_book[0]['age']


if __name__ == "__main__":
    print('age의 키값은? ',get_firsts_age())
    pass

'''
[] 는 array를 쓰는 대표 타입 (배열 초기화나 선언시 사용)
    arr = [] # 빈 배열을 만들 때 []사용
    arr = [1,2,3,4] #원소가 있는 배열을 만들 때 []사용

    arr[3] #배열의 3번째 원소에 접근할 때 []사용

() 는 tuple을 선언 초기화시 사용(원소 접근할때)
    mytuple = () #빈 튜플 생성할 때 ()사용
    mytuple = (1,2,3,4) # 원소가 있는 튜플을 만들 때 ()사용

    mytuple[3] # 튜플의 원소에 접근할 때 []사용
{} 는 dictionary의 대표 타입(딕셔너리 선언 및 초기화시 사용. (키에 대응하는 값 할당하거나 접근))
    mydictionary = {} #빈 딕셔너리 생성 시 {}사용
    mydictionary = {"mouse":3, "penguin":5}

    mydictionary["mouse"] # key("mouse")에 대응하는 value(3)에 접근할 때 사용
    mydictionary["cat"] = 1 # key("cat")에 대한 value(1) 생성

'''





'''
[쓰레기가 된 코드]
c_name_book=dict()    
    #print(type(name_book))
    #result = name_book["age"]    
    
    #for seq in len(name_book):
        #c_name_book += name_book[seq]
'''
