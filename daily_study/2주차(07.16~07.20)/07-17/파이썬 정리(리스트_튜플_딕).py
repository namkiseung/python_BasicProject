# -*- coding: cp949 -*-
<리스트>
1.리스트 만드는 방법(선언)
phone = ['apple', 'gallexy', 'samsung', [1,2,3,4,5]]

2.리스트 인덱싱
phone = ['apple', 'gallexy', 'samsung', [1,2,3,4,5]]
    2.1 각자안에 value가 튀어나온다.
    phone[0]
    phone[1]
    phone[3][1]
    phone[3][2]
    2.2 각자 문자열이 몇번째인지 나온다.
    phone['gallexy']
    2.3 리스트안에 담긴 str(문자열)을 인덱싱
    phone['gallexy'][1:]
    phone['gallexy'][1:5]
    2.4 인덱싱[]으로 접근해서 수정
    phone[3] = 'edit_text'
    2.4 리스트 사용방법 알아볼때
    dir(phone)
    2.5 리스트 요소 삭제, 빼내기(pop으로 마지막 요소 빼내기)
    phone.pop()         ->phone 출력시 pop()내용 빼고 나머지 내용들어있다.
    a=phone.pop()       -> a에 pop()으로 나온 하나의 문자만 들어간다
    phone.pop(1)     -> 리스트의[1] 의 value이 나온다(매개변수에 인덱스만 가능)
    2.5.1 삭제방법(2)
    phone.remove('apple')    -> (매개변수에 str값을 넣어서 중복되도 첫번째것만 제거)
    2.5.2 삭제방법(3)
    del phone[4]    -> 당연히 인덱스를 지정해 준다
    2.6 리스트 요소 추가하기(제일 뒤에 추가된다)
    phone.append('china')
    2.7 리스트에 포함된 요소 count 하기
    phone.count(x)      -> x가 리스트 내에 몇 개가 있는지 파악해 개수를 돌려준다
    2.8 리스트 순서 정렬하기
    phone.sort()  <-> phone.reverse()
    2.9 리스트 확장(extend)
    phone.extend([1,2]) 는  phone+=[1,2] 와 동

3.튜플(tuple) : 리스트와 다르게 [] 안쓰고 ()괄호를 사용한다
    t=(1,2,3,4,5)     -> 출력할때는 t[0] 이런식으로 한다
4.dict라는 사전(dictionary)
    d = {"dict":"사전", "ip":"아이피", "network":"네트워크"}
    4.1 keys()
        d.keys()로 사용하며, 키들을 list로 출력
    4.2 items()
        d.items()로 사용하며 dict에 담긴 키와 값의 쌍을 tuple list로 출력
    4.3 values()
    4.4 has_key()    :   괄호안에 "키 명"을 넣어 조회한다 true와 false로 반환됨
    



참고 : https://wikidocs.net/14
참고 교재 : 정보보안전문가 파이썬-i2sec
    
    
