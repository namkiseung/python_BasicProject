# -*- coding: utf-8 -*-


def smile(input_str):
    """ 문자열을 전달받아서, 문자열 내에 ee가 있으면, ee를 :) 로 치환해서 반환하는 함수를 작성하자
        (ee가 없으면 그대로 반환한다)
    
        sample in/out:
            smile("sleep") -> "sl:)p"
            smile("weekend") -> "w:)kend"
    """
    # 여기 작성
    for x in range(len(input_str)):
        if input_str[x:x+2] == 'ee':
            a = input_str.replace(input_str[x:x+2],':)')            
            #b = a.replace(a[x+1:x+2],')')            
            return a            
        else:            
            #문자열의 몇번째 위치에 탐색한 글자가 있는지 조사하자
            #해당 위치에 교환하자
            #결합해서 뽑자            
            #print input_str[x:x+2]
            #print x, x+2
            continue
            
    return 'success'
    


if __name__ == "__main__":
    print smile('sleep')
    print smile('weekend')
    pass

