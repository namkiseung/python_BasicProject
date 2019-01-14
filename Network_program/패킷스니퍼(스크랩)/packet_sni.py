# -*- coding: UTF-8 -*-
from socket import *

'''
(첫번째 인자) - 프로토콜 체계
AF는 Address Family, PF는 Protocol Family, 요즘은 AF로 통일
PF_INET IPv4 인터넷 프로토콜 체계
PF_INET6 IPv6 인터넷 프로토콜 체계
PF_LOCAL 로컬 통신을 위한 UNIX 프로토콜 체계
PF_PACKET Low Level 소켓을 위한 프로토콜 체계
PF_IPX IPX 노벨 프로토콜 체계
(두번째 인자) - 소켓의 데이터 방식
SOCK_STREAM : 연결 지향형, 데이터 경계가 없어 패킷 전송시 나눠 받을 수 있다. (No boundary)
데이터링크 계층에서 MTU값에 맞게 큰패킷을 작은패킷으로 Fragmentation 시킴. (보통1500 - 확인 : netsh interface ip show interface)
패킷 헤더에 DF(Do not Fragment)을 SET 하면 조각화 못시킴.
SOCK_DGRAM : 비연결 지향형, 데이터 경계 있어 전송한 횟수만큼 딱딱 받음.
SOCK_RAW : RAW 소켓
(세번쨰 인자) - 통신에 사용되는 프로토콜 정보 설정
IPPROTO_IP : 0으로 정의, 보통 이거 사용
IPPROTO_ICMP = 1
IPPROTO_RAW = 255
IPPROTO_TCP = 6
IPPROTO_UDP = 17
''' 
client = socket(AF_INET, SOCK_RAW,IPPROTO_ICMP) 
## 성공시 FD(File Descriptor) 반환 0-인풋 1-아웃풋 2-에러이나 파이썬은 소켓객체를 반환(객체안에 fd할당됨)

print(client)
name = gethostbyname(gethostname()) ## 외부아이피 가져옴
client.bind((name,0)) #소켓에 ip/port 주소 할당
client.ioctl(SIO_RCVALL, RCVALL_ON) ## 컴포넌트에 접근할 수 있게 통로 역할을 수행하는 IOCTL (입출력컨트롤) - 커널내 함수 사용할때
while True:
    RecvData = client.recv(1500)
    print(RecvData)
    bm = []
    for i in range(len(RecvData)) :
        bm.append(hex(RecvData[i]))
 
    print(bm)
client.ioctl(SIO_RCVALL, RCVALL_OFF) ## OFF시켜쥼
'''
Winpcap 드라이버가 없이 Winsock 으로 패킷 스니핑하는 방법 단, 네트워크계층 IP레벨의 모니터링 (ARP는 못잡음)
Raw소켓 생성 -> Bind -> WSAIoctl()에 SIO_RCVALL 로 TRUE(1) -> Recv()로 패킷 수신
nic promiscuous(무차별)모드로 변신!!
'''

