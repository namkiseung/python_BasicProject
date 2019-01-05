# -*- coding: cp949 -*-
import time, random
#첫 번째 배열을 기준 -> D F Y M J T U Q K Z
#(단, 전부 대문자)
#1차원 배열의 첫 번째 인덱스가 [0]=D일 때  1차원 배열의 순번을 기억해둔다.  (1)(2)
#해당 순번의 배열에서 두 번째 인덱스 [1]=F일 때  일치하는 순번을 기억해두자.
#해당 순번의 배열에서 세 번째 인덱스 [2]=Y일때 일치하는 순번을 기억해두자.
def rendom_str(): #처음 비교를 하기 위해 기준점을 세우는 사람생성(10개의 취미를 가진)
    res= '' #출력할 문자열
    for x in range(10): #열 번 반복
        ran=random.randrange(65,90+1) #65~90 index출력
        res+=chr(ran) #해당 인덱스에 해당하는 ascii 문자 반환
    return list(res) #10개 취미를 배열로 리턴
'''
선언 리스트 목록
1) 기준점 리스트(사람)
2) 기준점 리스트와 비교해서 일치하는 리스트(사람)들의 인덱스를 담는 리스트(매칭된 리스트)
3) 기준점 리스트로 쓰고 버려질 리스트들(이미 취미 매칭에 사용한 리스트)
4) 비교하고 몇 개가 일치하는지 적어둘 리스트
*2번 4번을 { dict } 로 담아두자.
'''
def manage_overlap(list_data):
    w_count = {}
    #lists = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 31, 31, 31, 32, 33, 33, 33, 33, 34, 34, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 40, 40, 40, 41, 41, 41, 42, 42, 42, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 45, 45, 46, 46, 46, 46, 47, 47, 47, 47, 48, 48, 48, 49, 49, 49, 50, 50, 50, 51, 51, 51, 51, 51, 51, 52, 52, 52, 53, 53, 53, 54, 54, 54, 54, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 57, 57, 57, 58, 58, 58, 59, 59, 59, 59, 60, 60, 60, 61, 61, 61, 61, 62, 62, 62, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 65, 65, 65, 66, 66, 66, 66, 67, 67, 67, 67, 67, 68, 68, 68, 68, 69, 69, 69, 70, 70, 70, 71, 71, 71, 71, 71, 72, 72, 72, 72, 73, 73, 73, 73, 74, 74, 74, 74, 75, 75, 75, 75, 75, 76, 76, 77, 77, 77, 77, 78, 78, 78, 78, 78, 79, 79, 79, 79, 80, 80, 81, 81, 81, 81, 82, 82, 82, 83, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 87, 87, 88, 88, 88, 88, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 94, 94, 94, 94, 95, 95, 95, 95, 96, 96, 96, 97, 97, 97, 97, 98, 98, 98, 98, 99]
    for lst in list_data: #리스트 데이터 반복하기
        #반환할 dict 타입의 인덱스에 삽입.(첫 번째 : 중복갯수, 두 번째, )
        try: w_count[lst] += 1  
        except: w_count[lst]=1 
    print(w_count)
    return w_count #딕셔너리 리턴
#해당 순번의 배열에서 열 번째 인덱스 [9]=Z일 때  일치하는 순번을 기억해두자.


def get_file_lines():
    data=''
    with open("C:/Users/namki/Desktop/python_BasicProject/algorithm/bridview_test/버드뷰_500x10.txt", "r") as f:
        data=f.read()
    return data

def res_num_compare(data):
    res={}
    for x in data: #딕셔너리 데이터를 반복 출력
        #value값을 비교해서 10부터~1까지 데이터가 있는지 비교
        for y in range(10,0,-1): 
            if data[x] == y: #value와 (10~7)중 일치확인
                #print(y) #일치하는 갯수 확인  #print(x)#일치하는 갯수에 해당하는 key를 출력
                #print("key : {}, value: {}".format(x, y))
                res[x]=y
                #time.sleep(0.1)
            else: #일치하지 않음
                pass
    return res
def high_match_index(datas):
    num_index=1
    while(True):
        if datas[0] == datas[num_index]:
            num_index += 1  #언젠가는 끝나게 되있기 때문에 계속 +1
        else:  #같지 않을때 num_index반환
            print("high_match_index함수에서 반환된 최고 매칭수: {} 명".format(num_index))
            return num_index
    
def result_formating(datas):
    #num_index에는 과연 매칭이 가장높은애가 몇 명인지 알려줌 
    result = list()
    datas=sorted(datas, key=lambda k : datas[k], reverse=True) #value를 기준으로 역정렬화
    num_index = high_match_index(datas) #선별된 매칭인원
    #join으로 출력데이터 사이에 '-'를 붙히기 위해 미리 배열에 저장해두자.
    #num_index개수 만큼 출력하자
    compare = 0
    for only_key in datas: #미리 정렬된 dict을 하나씩 빼자
        result.append(only_key)
        if compare == num_index: #이 조건문은 딱 최고로 매칭된 사람(key)만큼 출력하기 위해서 선언
            return result#매칭되지 않는 사람이 나오게 된다
        else: 
            compare += 1 #같은값이 처음부터 나오면 리턴값이 1개뿐이니 2개를 뽑기 위해 0부터 비교
    pass 
    '''
    가장 일치하는 대상자 2명 출력
    만일 3명이상이면 모두 출력
    [결과] value에 해당하는 key를 반환 (formatting해)
    3개이상 일치하나?--일치하는데 해당하는 data(dict 타입)을 담은 배열
    '''
if __name__=="__main__":
    play_cnt = 0#플레이 카운트
    try: #잘못된 input값의 예외처리
        coin = input("input : ")
    except:
        coin = 1
        print("잘못된 입력으로 임의의 숫자 '1' 이 입력되었습니다.")        
    coin = int(coin)
    while(play_cnt < coin):  #입력된 데이터 만큼 반복
        play_cnt+=1
        print("coin : {} play_cnt: {}".format(coin, play_cnt))
        data=rendom_str() #['Z', 'C', 'Y', 'A', 'F', 'X', 'U', 'Q', 'K', 'G']
        print("기준 : {}".format(data))
        pass_person=list()
        with open("C:/Users/namki/Desktop/python_BasicProject/algorithm/bridview_test/버드뷰_500x10.txt", "r") as f:
            res = f.readlines()
            for x in range(len(res)): #파일에서 가져온 row 수 만큼 반복해서 비교
                for y in data:
                    if y in res[x]:
                       print("결과는 true   사람 인덱스 {} ({})   일치 문자 : {}".format(x, res[x], y))
                       pass_person.append(x)#인덱스를 담자
                    else:
                        pass
            true_ing_list =manage_overlap(pass_person)#true에 반환된 리스트 가공
            res_dict = res_num_compare(true_ing_list) #true중에 나온 데이터를 인자로 넣어서 딕셔너리 리턴값(중복데이터와 : 중복숫자)
            matched = result_formating(res_dict) #가장 매칭이 잘 된 사람이 배열로 출력된다.
            #print("matched 출력해보자")
            #print(matched)
            #print(type(matched))
            print('-'.join(str(v) for v in matched))
        
            
                   
'''
    list_standard=list()
    list_already_usage=list()
    dict_result = dict()
    
        res_data = f.readline() #첫 번째 기준사람
        res_datas=f.readlines() #두 번째 이후 사람들 리스트
        list_standard = res_data.split()
        print(res_datas)
        for l_stand in f.readlines(): #비교될 대상 사람들
            print(l_stand)
            time.sleep(0.2)
            for t_num in range(len(res_data.split())): #한 사람의 취미 개수만큼 반복
                print(res_data.split()[t_num]) #한 사람이 가진 취미를 배열로 만들고 -> 기준배열에 넣기
                #비교 시작(다음번째 라인의 인덱스와 기준점 리스트의 인덱스)
                
                #if res_data.split()[t_num] == l_stand[t_num]
        
        #for x in  f.readlines():
         #   time.sleep(0.2)
         #   print(x)
'''         
        
'''
    res[0]==res[1]
    res[0]==res[2]
    res[0]==res[3]
    res[0]==res[4]
    res[0]==res[5]
    0번째에서 같지 않은 값이 나온다?
    -> res[1]==res[1]
    -> res[1]==res[2]
    -> res[1]==res[3]
    -> res[1]==res[4]
    -> res[1]==res[5]
    1번째에서 같지 않은 값이 나온다?
    ---> res[2]==res[1]
    ---> res[2]==res[2]
    ---> res[2]==res[3]
    ---> res[2]==res[4]
    ---> res[2]==res[5]
    2번째에서 같지 않은 값이 나온다?
    -----> res[3]==res[1]
    -----> res[3]==res[2]
    -----> res[3]==res[3]
    -----> res[3]==res[4]
    -----> res[3]==res[5]
    '''        

