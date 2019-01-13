#-*- coding:utf-8 -*-
#모듈설명 : 사용자가 옵션으로 입력한(host,port)대상으로 TCP커넥션 맺은 후, App의 배너를 가져오자.
#3개의 모듈(Main - PortScan - ConnScan)
import optparse
from socket import *
from threading import Thread
def PortScan(Target_Host, Target_Port):
    try:
        Target_IP = gethostbyname(Target_Host)
    except:
        print ("[-] Cannot Resolve '%s' : Unknown Host" % Target_Host)
        return
    
    try:
        Target_Name = gethostbyname(Target_IP)
        print("[+] Scan Result For : {}".format(Target_Name[0]))
    except:
        print("[+] Scan Result For : {}".format(Target_IP))
    setdefaulttimeout(1)

    for port in Target_Port:
        print("Scanning Port {}".format(port))
        t = Thread(target=ConnScan, args=(Target_Host, int(port)))
        t.start()

def ConnScan(Target_Host, Target_Port):
    try:
        #TCP커넥션을 위한 소켓을 만들자
        connskt = socket(AF_INET, SOCK_STREAM) #소켓 객체 초기화
        #연결시도 작업
        connskt.connect((Target_Host, Target_Port)) #소켓객체를 통해 connect함수호출.(실제 접속시도됨)
        connskt.send("")
        result = connskt.recv(1024) #소켓연결된 대상으로부터 수신한 데이터받는다.
        screenLock.acquire()
        print("[+] TCP OPEN {} \n {}".format(Target_Port, str(result)))
    except:
        #쓰레드 사용으로 인해 출력문이 한꺼번에 출력되지 않게 screen에 화면우선권 주자.(스레드당 하나만 출력)
        #screenLock.acquire() 
        print("[-] TCP closed {}".format(Target_Port))
        #print("Error name : {}".format(e))
    finally:
        #screenLock.release()
        #connskt.close()
        pass
def main():
    #optparser를 이용해 사용자에게 옵션을 제공함으로서 입력값에 대한 확장성을 보장한다.
    parser = optparse.OptionParser(usage="Usage Prog -H <Target_Host> -p <Target Port>")
    parser.add_option('-H', dest = 'Target_Host', type='string', help='specify target IP')
    parser.add_option('-p', dest = 'Target_Port', type='string', help='specify target IP')
    (options, args) = parser.parse_args()

    Target_Host = options.Target_Host
    Target_Port = str(options.Target_Port).split(',')

    if (Target_Host == None) | (Target_Port == None):
        print("[+] {}".format(parser.usage))
        exit(0)
    PortScan(Target_Host, Target_Port)

if __name__=="__main__":
    main()