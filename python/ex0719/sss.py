a = 0b11001100
b = 0b00110011
c = 0b01010101

print ''
print '[*] Bitwise operators'

print '[*] and, or, xor'
print 'a:{:08b}'.format(a)
print 'b:{:08b}'.format(b)
print ' a & b = {:08b}'.format(a&b)
print ' a | b = {:08b}'.format(a|b)
print ' a ^ b = {:08b}'.format(a^b)
print ' a ^ c = {:08b}'.format(a^c)
print ''

print '[*] shift left'
for cnt in range(8):
    print ' a << {} = {:08b}'.format(cnt, a<<cnt&0xff) 
print ''

print '[*] shift right'
for cnt in range(8):
    print ' a >> {} = {:08b}'.format(cnt, a>>cnt&0xff) 
print ''

'''
0x00000001  #닫기버튼 활성화
0x00000010  #최대화버튼 활성화

0x00000001 & 0x00000010 이렇게 되었을때, 시스템호출로 인해 최대화버튼과 닫기버튼이 동시에 뜬다.

[xor] : 상호베타로 서로 다른값일때 1, 같으면 0
0x00000001 xor 0x00000010   -> 이런식으로 암호화할때 사용하기도 한다.

major minor버전 나눠지는데, 자리수를 바뀌기위해서
    0000 0000         위 4비트 '0000'로 메이저 버전 아래 4비트로 마이너 버전
        0010  -> 메이저 버전이고
        0001  -> 마이저 버전이면, 아래 4비트는 
        이때 메이저와 마이너를 어떻게 나눌까?
        0xf 와 and연산으로 2개를 구분가능하다.


★ AND, OR, XOR로 비트수 계산하는 이유는 0001과 0010 등의 계산을 할때, 쓸데없는 자리들을 지워버리기위해 사용

'''