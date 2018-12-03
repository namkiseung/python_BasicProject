#-*-coding:utf-8-*-

##a = [1,2,6,7,8,9,10]
##a.append(3)
##a.append(4)
##a.append(5)
##a.sort()

##a.insert(2,3)
##a.insert(3,4)
##a.insert(4,5)

##a.extend([3,4,5])
##a.sort()

"""
튜플은 둥근 괄호를 사용한다.
튜플 변경 불가능한 타입이다.
"""
"""
t = (1,2,3,4,5)

##예제 (1)
def func():
    tax = 5
    price = 1500
    total = 1050
    return price, total, tax

p, t, ta = func()  #방법1
result = func() #방법2
result[0]
result[1]
result[2]
"""

'''
dict이란 사전이다.
무언가 값을 찾고 싶을때, 찾을 수 있다.
ex) {"dictionary":"사전"}
         키(key)   값(value)


(immutable)
'''
#####dict을 배우자
new_d = dict()


new_d["number"] = range(10)
new_d["chars"] = 'abcdefg'
new_d["special_char"] = '!@#$%'

new_d['chars'] = 'ab'
new_d['chars'] = 'a'
new_d['chars'] = 'acs'
#값을 list라는 타입으로 넣을 수 있다 (그렇게 되면 list의 메서드를 사용가능)
new_d['iflist']=[1,2,3]
            #new_d['iflists']=[1,2,3,4].append('@@')
#dict에서 key값만 찾아보자
    #print (new_d.keys())
#dict에서 value값만 찾아보자
    #print (new_d.items())

#10 in range(20)
# a in range(b)  -> a가 range인 b에 포함되어 있나? true, false 반환

#print new_d.has_key("chars")      #해시값이 있는지 참 거짓 확인

#자료형 boolean bool






    #1. port 라는 dirt()형을 만들자
    #2. dirt() 형에 키값을 3개를 만들자
    #   2.1 'well_port' = 0번 ~ 1023
    #   2.2 'registered_port' = 1024번 ~ 49151번
    #   2.3 'dynamic_port' =  49152번 ~ 65535번
port_num = dict()
port_num={"well_port" : range(1024),
         "registered_port": range(1024, 49152),
         "dynamic_port": range(49152, 65536)}

print "well_port는  ",port_num['well_port'][-5:]
print "registered_port는  ",port_num['registered_port'][-5:]
print "dynamic_port는  ",port_num['dynamic_port'][-5:]




































