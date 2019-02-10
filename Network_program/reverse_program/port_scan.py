import sys
from socket import *

host = sys.argv[1]
ports = sys.argv[2].split('-')
start_port = int(ports[0])
end_port = int(ports[1])
#host에 대한 ip를 반환받자.
target_ip = gethostbyname(host)
#오픈된 포트를 담을 리스트
opened_ports = []
for port in range(start_port, end_port):
        sock = socket(AF_INET, SOCK_STREAM) #ipv4와 TCP통신 sock객체 만들자.
        sock.settimeout(3)
        result = sock.connect_ex((target_ip, port))
        if result == 0: #만약에 포트가 열리면 return으로 0이 나온다.
                opened_ports.append(str(port))

print('open port : '+', '.join(opened_ports))
