#-*- coding:cp949 -*-
network_port = {
    "well_known" : range(0,1024),
    "registed" : range(1024,49152),
    "dynamic" : range(49152,65336),
    }

port = input()
if port in network_port["well_known"]:
    print('well_known')
elif port in network_port["registed"]:
    print('registed')
elif port in network_port["dynamic"]:
    print('dynamic')
else:
    print('not found')


#문자의 첫 위치를 알아낸다(없으면 -1 반환해준다)
#즉, index는 에러를 일으키면 프로그램 진행안되니 find사용
