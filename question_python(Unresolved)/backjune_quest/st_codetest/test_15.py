'''
>>네 수의 합 개요
    주어진 자연수를 4개의 자연수의 합으로 
    나타내는 경우의 수 구하자.
    (이때 자연수의 순서를 바꿔서 같아지는 경우는 하나로 간주)
'''

#입력받는 정수가 1보다 작으면 존재하지 않음
def get_number(get_num):
    max_num = int(get_num)
    list_num=list()
    count=0
    for x in range(1, max_num+1):
        count+=1
        #만일 
        #입력받은 정수에서 -1을 빼 리스트에 담는다.
        list_num.append(int(get_num))
        int(get_num)-=1
        if get_num < 1:
            for x in int(list_num):
                print("[+] print output num {}\n".format(x))
            return list_num

if __name__=="__main__":
    #정수를 입력받는다.
    get_num=input("num :")
    num=int(get_num)
    get_number(num)
'''
>>입력
입력은 여러 개의 테스트 케이스로 구성되어있다. 
첫 줄에는 테스트 케이스의 개수가 주어진다. 
다음 줄부터 각각의 테스트 케이스가 별도의 줄에 주어진다.

>>출력
각각의 테스트 케이스에 대해 경우의 수를 출력한다.
'''