# -*- coding: cp949 -*-
##작업목록은 리스트로 정리하기 좋은데,
##이때 pop으로 처리하고 처리하고 마무리 하는게 좋다
'''
list 의 함수들
    count 글ㅉ씨 소개
    append 리스트에 내용 추가
    extend 리스트 확장할떄
    index
    insert 내가 넣을 위치 정할수 있다
    pop 젤 뒤에 있는얘 꺼낸다
    sort 정렬해준다
    reverse 정렬한것을 반대로 한다
    remove(value) 삭제해준다
    del 삭제


    sort()
    reverse()
    '''
#####my_list = [1,2,3,4,5]
#####print my_list[:-1]
##
##i2sec_urls = ["www.i2sec.co.kr","seoul.i2sec.co.kr","daegu.i2sec.co.kr",]
###print i2sec_urls[0].index('i2sec')
##i2sec_urls.append(1)
##i2sec_urls.append(10)
##i2sec_urls.append(100)
##
##
###print i2sec_urls.pop(-1)
##
##
##
###i2sec_urls.insert(i2sec_urls.index(100),3)
##i2sec_urls.remove(1)
##i2sec_urls.reverse()
##print i2sec_urls
##
##
##print len(i2sec_urls)
##
##i2sec_urls.sort()
##print i2sec_urls
##
##i2sec_urls.reverse()
##print i2sec_urls

############################################################
a = [1,2,6,7,8,9,10]
#a.append(3,4,5)
a.extend([3,4,5])
a.sort()
print '1번 답',a
############################################################
well_known_port = [1,7,9,13,17,19,20,21,22,23,24,25]
############################################################
well_known_port.reverse()
print '3번 답',well_known_port
############################################################
aa = [1,2,3,4, 1,2,3,4, 1,2,3,4]
   #[1,2,3,4, 2,3,4, 2,3,4] 로 만들기
aa.reverse()
aa.remove(1)
aa.remove(1)
aa.reverse()

print '4번 답',aa
#reverse -> 작업 -> reverse



#str 타입을 모두알아와라




