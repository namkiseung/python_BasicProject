import argparse,os
import sys,subprocess
import threading
from datetime import datetime
#from time import sleep

#python3 scan_tool_20200403_001.py -spt 1 -dpt 65535 -ds url_list.txt
#python3 scan_tool_20200403_001.py -spt 1 -dpt 65535 -ds url_list_002.txt
#python scan_tool_20200402_002.py -spt 1 -dpt 65535 -ds url_list.txt

#nohup python3 scan_tool_20200407_001.py -spt 25501 -dpt 65535 -ds url_list.txt > nohup.out_url_list.txt 2>&1 &
#nohup python3 scan_tool_20200407_001.py -spt 25001 -dpt 65535 -ds url_list_002.txt > nohup.out_url_list_002.txt 2>&1 &
#nohup python3 scan_tool_20200407_001.py -spt 1 -dpt 65535 -ds url_list_003.txt > nohup.out_url_list_003.txt 2>&1 &

# 메인 파라미터 파싱
def argvConf(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument('-spt', required=True, default="10000")     # 시작 포트
    parser.add_argument('-dpt', required=True, default="10010")     # 끝 포트
    parser.add_argument('-ds', required=True)                      # ip 대상 텍스트
    args=parser.parse_args() 
    return args

# 포트스캔 IP 대상 읽기
def readList(ipListTxt):
    file = open(ipListTxt,'r')
    lines = file.read()
    lines = lines.rstrip()
    print("[log IP List]\n{}".format(lines))    
    file.close()
    return lines.split("\n")

# 포트스캔 수행
def portScan(ipValue, minPort, offsetPort):
    portList = []
    for i in range(int(minPort), int(offsetPort)+1):
        portList.append(i)    
    _cmd = "sudo mkdir -m 755 ./{}".format(ipValue)
    _result = subprocess.check_output(_cmd, shell=True)
    
    section = 100
    # 입력 받은 포트 옵션으로 100개씩 구간 나누기
    portSection = [portList[i * section:(i + 1) * section] for i in range((len(portList) + section - 1) // section )] 
    # nmap 설정을 위하여 구간별 최소, 최대 포트 번호 확인
    for i in range(len(portSection)):
        _portMinSection = portSection[i][0]
        _portMaxSection = portSection[i][-1]
        time = datetime.today().strftime("%Y%m%d%H%M%S")
        cmd = "sudo proxychains nmap -sS -PN -n -sV -r -T5 -p {}-{} --scan-delay 1s -oX ./{}/{}_{}-{}".format(_portMinSection, _portMaxSection, ipValue, ipValue, _portMinSection, _portMaxSection) + "_" + time + ".xml {}".format(ipValue)
        result = subprocess.check_output(cmd, shell=True)
        print(cmd)
#        sleep(5)

"""# tcpdump, 시간 기록 예정
def tcpdump(ip, gettime):
    proc=subprocess.Popen("sudo tcpdump -i eth0 dst {} -w {}-{}.pcap".format(ip, ip, gettime), shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
    return proc
"""

if __name__ == '__main__':
    args = argvConf()
    ipList = readList(args.ds)
    minPort = args.spt
    offsetPort = args.dpt

    for index, ipValue in enumerate(ipList, start=1):
        _handler = threading.Thread(target=portScan, args=(ipValue, minPort, offsetPort))
#        sleep(5)
        _handler.start()

