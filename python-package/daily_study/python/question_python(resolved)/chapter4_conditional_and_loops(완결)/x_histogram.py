# -*- coding: utf-8 -*-

def histogram(int_list):
    """ 양의 정수 데이터(리스트 형)를 전달받고, '*' 로 히스토그램을 만들어 반환하는 함수를 작성하자
        ("\n"로 잇는다 print로 출력하면 화면에 그려지도록)

        sample in/out:
          histogram([2,3,6,5]) -> "**\n***\n******\n*****"
          histogram([1,2,3,2,1]) -> "*\n**\n***\n**\n*"
    """
    # 여기 작성
    '''
    int_list[0]이 2면  **     끝나고 '\n'
    int_list[1]이 3면  ***        끝나고 '\n'
    int_list[2]이 6면  ******        끝나고 '\n'
    int_list[3]이 5면  *****   끝나고 '\n'
    '''
    a=''
    x=0
    while True:
        for count in int_list:
            print count*'*'
        x+=1        
        if len(int_list) > 1:
            return ''
        

##    r=[]
##    for c in int_list:
##        h="*"*c
##        r.append(h+'\n')
    return ''

if __name__ == "__main__":
    list_input = [2,3,6,5]
    histogram_list = [1,2,3,2,1,5,4]
    print histogram(list_input)    
    print histogram(histogram_list)    
    
    
    pass
