# -*- coding: utf-8 -*-


def print_dict(input_dict):
    """ 입력된 dict의 키와 값을 아래와 같이 문자열로 만들어 반환하는 함수를 작성하자

        sample in/out:
            print_dict({"ham":"yes", "egg":"yes", "spam":"no"}) -> "(1) egg -> yes\n(2) ham -> yes\n(3) spam -> no"
    """
    # 여기 작성
    #dict의 키 마다 키앞에 '(cnt++)' 문자가 들어가야되고
    #re_key = input_dict.keys()
    #re_val = input_dict.values()
    a=input_dict.items()      # 딕셔너리의 아이템들 (아이템은 [1]이랑 [1][1]로 키와 아이템을 각각 만질수 있음)
    b=input_dict.keys()       # 딕셔너리의 키들을 b에 리스트형으로 담음

    
    cnt = 0   #괄호안에 카운트
    for x in range(len(b)):    
        cnt += 1
        print '('+'{0}'.format(cnt)+')'+'->'.join(a[x])+'\n',
    
    #[출력 시나리오]
    # print '('+cnt+')','->'.join(a[1]),'\n'    
    # print '('+cnt+')','->'.join(a[2]),'\n'    
    # print '('+cnt+')','->'.join(a[3]),'\n'
    return ''

    
 


if __name__ == "__main__":    
    sample_dict={"ham":"yes", "egg":"yes", "spam":"no"}
    print print_dict(sample_dict)     
    #결과"(1) egg -> yes\n
    # (2) ham -> yes\n
    # (3) spam -> no"
    pass

#values의 뒤에  '\n' 문자를 삽입해줘야된다
    #print '-'.join(re_key)   -> 조인은 원하는곳에 문자를 입력하기 힘듬...
    #format