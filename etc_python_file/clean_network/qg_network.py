# -*- coding: utf-8-*-
import qg_network_q

def seq_question_input(select_num):
    if select_num == 1:
        return ''' source address
destination address
data'''
    elif select_num == 2:
        return '''language = protocol( Timing ) '''
    elif select_num == 3:
        return '''(Sequence Number)
protocol -> 순서지정 -> "여 보 세 요" '''
    elif select_num == 4:
        return ''' 유선 - 1500 byte 
무선 - 2312 byte'''
    elif select_num == 5:
        return ''' Fragment Number'''
    elif select_num == 6:
        return ''' - 표준/비표준 (사투리) '''
    elif select_num == 7:
        return '''컴퓨터과 통신하는데 7번의 과정을 거친다.
	ex) 보낼때 : 카톡할때 : 응용프로그램(앱, 어플) [ 7->6->5->4->3->2->1 ]
	ex) 벗긴다 : 1층겉에가 보인다'''
    elif select_num == 8:
        return '''Local Area / Metro Area / Wide Area '''
    elif select_num == 9:
        return ''' 1. 물리계층 : (장비:케이블,리피터,허브)       (단위 : bit)
	(QR.허브 : 컴퓨터를 연결해주는 장치)'''
    elif select_num == 10:
        return ''' 2. 데이터링크 : MAC주소 사용 (장비:브릿지,스위치) (단위:Frame)
	(QR.브릿지 : 여러 개의 네트워크 세그먼트를 연결해 준다)
	(QR.스위치 : 네트워크 선을 묶는다. 그리고 MAC주소를 알기때문에 연결해준다)
	(QR.이더넷 : mac주소를 기반으로 통신한다)'''
    elif select_num == 11:
        return ''' 3. IP주소 : (역사 : MAC주소로는 통신힘들어서 나왔다) (장비 : router)'''
    elif select_num == 12:
        return '''4. TCP와 UDP 통신 설명 혹은 비교
	-3way알고왔냐? (그럼주로 TCP는 뭐가있냐)(UDP에 공격 DrDos)(Wellnone port)
	-tct : 컴터끼리 통신하는 언어
	-http : 컴퓨터안에 프로그램끼리 통신하는언어 '''
    elif select_num == 13:
        return '''  웹 서버는 정적인 데이터를 처리하는 서버이다. 이미지나 단순 html파일과 같은 리소스를 제공하는 서버는 웹 서버를 통하면 WAS를 이용하는 것보다 빠르고 안정적이다(왜? 다른 글 소스로 써볼까?) WAS는 동적인 데이터를 처리하는 서버이다. DB와 연결되어 데이터를 주고 받거나 프로그램으로 데이터 조작이 필요한 경우에는 WAS를 활용 해야 한다.  두 서버의 목적의 차이 때문에 두 개의 서버를 연동해서 사용하면 더욱 효과적인 서비스를 제공할 수 있다. 사용자 요청은 http 웹 서버를 통해 받고 내부 프로그램은 was를 통해 처리하는 식으로 한다면 정적인 데이터와 동적인 데이터를 효과적으로 처리가 가능할 것이다. '''
    elif select_num == 14:
        return '''1. ARP 스푸핑(중간자하면 내가 세션만들수있다), 2.세션하이재킹, 3.슬로리스 공격 등 '''
    elif select_num == 15:
        return ''' <컴퓨터 프로그램이 통신하는 구간>6 - 암호화,복호화
5 - 에러발생시 복구 세션관리
7 - 사용자 인터페이스 '''
    elif select_num == 16:
        return '''TCP/IP 계층
1층 ([1,2] 네트워크 인터페이스 계층) - MAC주소 통신
2층 ([3] IP계층) - IP주소 통신
3층 ([4] TCP/UDP계층) - port통신
4층 ([5,6,7] 응용프로세스 계층) '''
    elif select_num == 17:
        return ''' csma/cd(유선) : 한가한지 살펴본다 -> 한가하면 데이터 보내고 -> 보낸데이터에서 충돌확인 : [목적 : 목적지 까지 갔는지 가다 충돌났는지 확인위해사용(같은대역)]
csma/ca(무선) : 각 스테이션들이 번갈아가며 통신하도록! [목적 : 충돌을 회피]'''
    elif select_num == 18:
        return ''' - 32비트 길이
- 지역이름(대역)이 숨어있고, 그 안에 몇번째 컴퓨터인가가 나와있다(서브넷마스크)'''
    elif select_num == 19:
        return '''1. 여러 개 외부 라우터를 돌아다닌다.
2. 빠른길로 라우팅(라우터 끼리 정보를교환)
3. 장소(네트워크) 간 이동(인터넷을 가는데 여러 네트워크를 지나가기때문)
4. 그래서 라우터란? 네트워크(장소)와 네트워크를 연결시키는 문 (라우터 게이트웨이)
5. 장소를 장소를 연결해주기 때문에 그 지역의 이름을 알아야한다.
6. 공유기를 새로 연결했는데, 인터넷마비왔다? -> 라우터 이름충돌 '''
    elif select_num == 20:
        return '''-공유기 가지고 만든 내부 네트워크
-10.0.0.0/8 | 172.16.0.1 ~ 172.31.255.255 | 192.168.0./024 '''
    elif select_num == 21:
        return ''' -인터넷으로 만든 네트워크'''
    elif select_num == 22:
        return '''-라우터의 공유기능
-네트워크 주소 변환 '''
    elif select_num == 23:
        return ''' -IP주소
-서브넷마스크
-기본 게이트웨이
-DNS주소'''
    elif select_num == 24:
        return '''-자동으로 IP 서브넷마스크 G/W DNS 불러주는 기능이며, 라우터가 하는일
<리눅스에서 설정>
1. ifconfig [장치이름] [IP주소]
ex) ifconfig eth0 192.168.0.100

<IP주소 서브넷 마스크 설정>
ex)ifconfig eth0 192.168.0.100 netmask 255.255.255.0

<게이트웨이 주소 알려주자>
route add default gw 192.168.0.1

<DNS주소 불러주자>
"명령어보단 파일을 수정한다"
vi /etc/resolve.conf 여기에서 namesever 8.8.8.8 '''
    elif select_num == 25:
        return ''' ★ARP : 네트워크통신의 첫번째 과정에서 IP주소를 가지고 MAC주소를 찾는다.
(사람은 IP를 불러주고, 운영체제상은 MAC으로 통신중이니까 ARP 사용)
과정 1 :주변모두에게 물어보는 과정
과정 2 : 응답오는 과정'''
    elif select_num == 26:
        return '''port를 이용한 통신을 안한다!! '''
    elif select_num == 27:
        return '''- 세션 개념있는지
- 3 way handshaking(살아있냐? -> 살아있다 왜? -> 통신하자) 그 다음 http 통신(get,post)
- SYN -> SYN+ACK -> ACK (port를 사용해 통신) == > 세션이 성립되고, C가S에게 자료달라고할 수 있다.
- 방화벽정책시 TCP에서 SYN을 찾을때는 몇 번 포트를 먼저 찾을지 봐야한다. '''
    elif select_num == 28:
        return '''-침투 대상 서버 상태 확인
-서비스 내역 및 활성화 상태 확인 '''
    elif select_num == 29:
        return '''-희생자가 알고 있는 mac변경
-리플라이 공격으로 변조 시도
-공격자가 통신흐름 바꿔서 중간자공격 가능 '''
    elif select_num == 30:
        print '''- openssl에서 세션유지 겸 하트비트 프로토콜 사용하는데, 데이터 요청할때 데이터 길이도 같이보낸다.
길이 값을 조작하여 생긴 취약점 '''
    elif select_num == 31:
        print ''' -icmp를 이용한 DrDoS
-보안 : 목적지가 브로드캐스트로 보내는 핑을 찾아서 없애자.'''
    elif select_num == 32:
        print ''' 시간을 물어보면 시간을 대답해주는데, monlist를 이용한다.'''
    elif select_num == 33:
        print ''' 누군가 대량으로 any로 물어보면 다수의 대답이 나가는 공격'''
    elif select_num == 34:
        print ''' '''
    elif select_num == 35:
        print ''' - 아파치 대상으로하는 공격(최대 1000개)
 - 연결에 관련된 공격 '''
    elif select_num == 36:
        print '''- Rogue AP(내부에 유션 네트워크에 연결된 불법 AP) -> 설정취약하기에 공격표적이됨
- Ad-Hoc 은 대표적으로 프린터(유무선되는)를 경유해 내부침투한다
- phising AP : (1)그냥 Ap만들었더니 낚 (2)프로브로 낚 (3)신호 세게해서 AP에 연결
- WEP/WPA Crack :
- MAC Spoof : AP에 접근하는데 AP의 보안설정 불가로 MAC변조
- Mis-Config AP : 보안설정 미흡한 AP존재할때
- DoS : 스테이션에게 서비스 못받게 하는 패킷(디오디케이션, 디오솔리케이션)사용 '''
    elif select_num == 37:
        print ''' - 공격자 추적힘듬
- 대응방안이 없다'''
    elif select_num == 38:
        print ''' -스테이션과 통신시 암호화패킷으로 주고받는다.
-알고리즘 방식은 RC4고, Key라는 값은 비번을 아스키로 변환해서 사용
-Key를 알면 비번을 유추가능
-암호화된 패킷 수집(많이)해서 RC4로 돌리면 IV와 KEY를 합친것 아는데
-IV많이 수집해서 합친거에서 IV를 빼면 추리가능

-가짜인증
-데이터 유발
-크랙 시작'''
    elif select_num == 39:
        print '''-해커가 인증 응답 패킷 수집
-거기에 어떤 암호화된 키가 맞다 아니다 나오는데 이 정보로 무차별 공격 '''
    elif select_num == 40:
        print '''-인사는 애매하면 먼저하자.
1.커뮤니케이션,프리젠테이션
2.기획/문서 작성능력(오피스 활용, 국어)
3.긍정적인 마인드(도전정신, 자신감)
4.영어(라푼젤)
5.끈만 놓지말자
6.아주작은거부터시작
* 장애 발생 시 대응 요령 -> 마련보내기'''
    elif select_num == 41:
        print '''-메일(1) : "i2sec자료소개서 주세요" ->  "i2sec회사 소개자료건입니다" | "i2sec이력서 주세요" -> "i2sec ~ 이력서 건입니다"
-메일(2) : 노트패드에 메일 작성하고 -> 가지치기 하자.
-메일(3) : 정확하게 못먹어도 고
-메일(4) : 메일 보내고, 2차로 연락해서 메일보냈다고 말하기
-메일(5) : 참조(CC)할사람은 꼭 해야한다. '''
    elif select_num == 42:
        print ''' -보고서(1) : 출력해서 확인
-보고서(2) : 국어
-보고서(3) : 색 2개'''
    elif select_num == 43:
        print '''-PT (1) : 뒤를 보면 안돼
-PT (2) : 가족이나, 거울 연습(하루아침X)
-PT (3) : 시선처리(사시)
-PT (4) : 스토리텔링(초반 빌드업)->프리진브레이크
-PT (5) : "질문받으면 좋다~라고하기" '''
    elif select_num == 44:
        print ''' '''
    elif select_num == 45:
        print ''' '''
        
    
if __name__=="__main__":
    print qg_network_q.default_sentence()
    while True:        
        data=int()
        "질문 다시 보려면 1입력 / 종료하시려면 -1을 입력"
        data = input("number : ")
        print seq_question_input(data)
        print ''
        if data == -1:
            break
        elif data == 0:
            print qg_network_q.default_sentence()
