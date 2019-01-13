import os
 
def get_nmap(options, ip):
    #nmap명령어와 옵션, IP할당하기
    command = "nmap" + options + " " + ip
    #명령어실행
    process = os.popen(command)
    #결과 리턴
    result = str(process.read())
    return result
 
if __name__ == '__main__':
    print(get_nmap(" -F", "180.80.93.117"))