# -*- coding: utf-8 -*-


def is_unique(input_list):
    """ 리스트를 전달받아서, 리스트에 담긴 요소들이 모두 다른 값인지(중복된게 없는지)를 True/False로 반환하는 함수를 작성하자

        sample in/out:
            is_uniques([2,4,5,7,9])     -> True
            is_uniques([2,4,5,5,7,9])   -> False
    """
    # 여기 작성
    #a=''
    #solt = -1
    #last=len(input_list)
    #input_list.reverse()
    #double_num = input_list[0]          
    
    #리스트의 첫번째 값을 기준으로
   # 리스트의 첫번째 값부터 끝까지를 비교해서 
    #중복되는게 있는지 확인
                 
        # for x in input_list:           
    #     solt = solt+1          
    #     if not x == double_num:     
    #         print x,'and',double_num
            # 총 5자리중 
            #   1    ==    1-5
            #   2    ==    2-5
            #   3    ==    3-5
            #   4    ==    4-5                                    
        #     a = 'True'
        #     pass
        # else:
        #     a = 'False'                                
        #     break
    #input_list.count(input_list[9])
    #print input_list.count(input_list[1])
    
    #input_list2 = input_list
    #input_list3 = input_list2
    
    
    #tmp = input_list2[input_list3[0]]   #input_list3의 마지막에 입력된 값 
    #print tmp

    tmp_list=list()
    for x in input_list:
        if x in tmp_list:
            return False
        else:
            tmp_list.append(x)

    return True
#중복 false
        


    # for x in input_list:                                    
    #     b = input_list.count(x)        
    #     if b > 1:
    #         return False
    #     else:
    #         print True
    #         pass
    


if __name__ == "__main__":
    list_1=[1,2,4,5,7]
    list_2=[2,4,5,5,7,9]
    
    print is_unique(list_1)
    print is_unique(list_2)
    pass

