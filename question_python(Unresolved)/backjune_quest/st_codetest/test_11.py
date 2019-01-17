'''
>>추석개요
    원택님이 돈을 다잃음(실력이 없거나, 운이 없거나)->'집착시작'

    추석이후 원택님은 3개 받았다. 선물상자를
    상자안에는 송편이 한 줄로 길게 있었다.

    (원택님)뚫어지게 쳐다보면서 든생각  
    "(1) 3박스에 다른 송편이 들어있는데, 글자가 똑같은 걸들도 있다."
    "(2) 한 줄이니까 문자열이다."
    "(3) 공통인 문자열 찾을 수 있지 않을까?"
    "(4) 나아가 공통으로 있는 문자의 최대 길이는 얼마인가 궁금"
'''
if __name__=="__main__":
    print("write only [String] and wanted exit is 'q'")
    first_str="" #s1과 s2 공통문자들
    second_str="" #s1+s2 공통문자열과 s3문자열의 공통문자들
    start=0
    while True:
        if start == 1:
            break
        #비교할 문자열
        s1_datas=""
        s2_datas=""
        s3_datas=""
        s1_datas=input("string 1 :")
        s2_datas=input("string 2 :")
        s3_datas=input("string 3 :")
        #단, 조건(문자열 길이 100미만)
        if len(s1_datas) > 99 or len(s2_datas) > 99 or len(s3_datas) > 99:
            break
        #1. s1,s2문자열을 비교하자.
        for s1_data in s1_datas:
            for s2_data in s2_datas:
                #2. 공통문자열을 만들자
                if str(s1_data) == str(s2_data):
                    first_str += str(s1_data)
        #3. 공통문자열과 s1문자열을 비교하자.
        for s1s2_data in first_str:
            for s3_data in s3_datas:
                if str(s1s2_data) == str(s3_data):
                    second_str+=str(s1s2_data)
        #4. 마지막에 공통된 데이터의 길이 출력or리턴
        print(len(second_str))
        start+=1    
'''
>>입력
    S1,S2,S3 문자열 타입변수(단, 길이는 100미만)

>>출력
    각 문자열 변수에서 가장 긴 공통 부분의 길이를 출력한다.
    (단, 테스트 케이스마다 별도의 줄에 정답 입력)
'''