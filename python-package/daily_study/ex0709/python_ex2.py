# -*- coding: cp949 -*-

#print '\n'*25
#print "가", '나'
#print "1 + 1 =", 1+1
#print문이 Print prinT 등 대소문자 구분한다
from datetime import datetime
now = datetime.now()

print '이름은',
#val = input()  #문자는 raw_input()
val=1
print val
print('%s년 %s월 %s일 %s시 %s분'%(now.year, now.month, now.day, now.hour, now.minute))
print "i2sec에는 매점이 어디있나요?"
print "강의실에 과자랑 빵이", '학생 수 만큼', '배치 되어 있으면', '좋겠다'

#데이터 타입 알아볼때 type()
#숫자,문자를 16진수로 바꿀떄 print hex(6511) / print bin(54444)

#print ord('h'),ord('e'),ord('l'),ord('l'),ord('o'),ord(' '),ord('w'),ord('o'),ord('r'),ord('l'),ord('d')
print chr(104),chr(101),chr(108),chr(108),chr(111),chr(32),chr(119),chr(111),chr(114),chr(108),chr(100)

#문자를 아스키코드로 알기 위해서 print ord("a") 로 ascll코드를 얻자
