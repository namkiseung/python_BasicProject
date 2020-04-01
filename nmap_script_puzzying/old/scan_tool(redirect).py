import argparse,os, time, datetime
import sys,subprocess
import threading
from queue import Queue

class Scan_duplication(threading.Thread):
    def __init__(self, time):
        super(Scan_duplication, self).__init__()
        self.time = time
        self.start()
            
    def run(self):
        #time.sleep(0)
        #print(self.time, " seconds start!")
        '''for i in range(0,self.time):
            time.sleep(0)
            print("0 sec of {}".format(self.time))'''
        return "[*overriding*] {} seconds finished!".format(self.time)
        
def argv_conf(): #make configure of argvs-object 
    parser = argparse.ArgumentParser() #define instacne
    parser.add_argument('-ip', required=False)
    parser.add_argument('-o', required=True, default="result")
    parser.add_argument('-spt', required=True, default="10000")
    parser.add_argument('-dpt', required=True, default="10010")
    parser.add_argument('-ds', required=False)
    args=parser.parse_args() #argv parsing
    return args
def measure_timeClocks(time,standard_time):
    time = time.perf_counter() #usage function python3.3~
    return (time-standard_time) #return variable of measure time
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    #display progress bar
    formatStr = "{0:." + str(decimals) + "f}" 
    percent = formatStr.format(100 * (iteration / float(total))) 
    filledLength = int(round(barLength * iteration / float(total))) 
    bar = '#' * filledLength + '-' * (barLength - filledLength) 
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)), 
    sys.stdout.flush()
    
def processing(ip,sport,dport,fname,_cmd,startTime,gettime):
    #Port-Scanning (1)input datas (2)exec cmd (3) make output-files (4) display processbar (5) record time
    fname="{}-{}".format(fname, ip)
    #os.popen("touch ./tmp/{}.txt".format(fname)).read()
    #result=list()
    try:
        _cmd=_cmd+" >> {}.txt".format(fname)
        print("[**] cmd : {}".format(_cmd))
        p = subprocess.Popen(_cmd, shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        #files=open("./tmp/{}.txt".format(fname),"a")
        #for line in p.stdout.readlines():
        #    print(line.decode('euc-kr')) #result.append(line.decode('euc-kr'))
        #    files.write("{}".format(line.decode('euc-kr')))
        #files.close()          
          
    except Exception as ex:
        print("[*] error", ex)
    finally:
        endTime = time.time() - startTime
        endTime = time.ctime(endTime)
        print("[*] endTime : {}".format(endTime))

def dataset_url(dataset):
    domainset=list()
    f = open(dataset, 'r')
    lines = f.read()
    lines=lines.rstrip()
    print("[log dataset]:{}".format(lines))
    f.close
    return lines.split("\n")

if __name__=="__main__": #main function line
    min_port = 1
    max_port = 65535
    args=argv_conf()
    startTime = time.time()
    gettime=datetime.datetime.today().strftime("%H%M-%S-%y%m%d")
    #print(gettime)
    '''
    #dataset에서 1개 IP 나올떄 마다 function called name of the processing 
    #call single ip
    #processing(args.ip, args.spt, args.dpt, args.o, startTime, gettime)
    #call multi ip inside dataset
    '''
    threads = []
    idx=0
    dataset_args=args.ds
    dataset=dataset_url(dataset_args)
    min_port = args.spt
    offset_port = args.dpt
    #ex) 1-1023 / #901 ~ 1000 / #1001 ~ 1100 / 1001-
    scan_cnt=0
    
    #init queue
    q = Queue(maxsize=20)
    #결국에는-> processing(ip, min_port, offset_port, args.o, cmd, startTime, gettime)
    for ip in dataset:
        idx=idx+1    
        #print("[*] count: {} | cmd : {}".format(idx, "sudo proxychains nmap -sS -PN -n -sV -r -T5 -p {}-{} --scan-delay 0 {}".format(min_port, offset_port, ip)))
        while True:
            min_port = int(min_port)+100 #101->201->301....901->1001->...65301->65401->65501
            if int(min_port) < 0 or int(offset_port) < 0 or int(min_port) > 65535 or int(offset_port) > 65535 or int(offset_port)-int(min_port) < 0:
                break
            elif int(min_port) < 105: #처음만 1~100 포트 스캔
                #print("[elif문] elif int(min_port) < 105")
                cmd = "sudo proxychains nmap -sS -PN -n -sV -r -T5 -p {}-{} --scan-delay 1 {}".format(min_port-100, min_port-1, ip)
                threads.append(cmd)
                continue
            elif int(min_port) > 101 and int(min_port) < 65535: #나머지는 시작포트와 끝포트의 값이 100씩 더해진다
                if int(offset_port) == int(min_port):
                    #print("[elif문의 if문] int(offset_port) == int(min_port)")
                    cmd = "sudo proxychains nmap -sS -PN -n -sV -r -T5 -p {} --scan-delay 1 {}".format(min_port, ip) # 65435
                    threads.append(cmd)
                    printProgress(idx, len(dataset), 'Progress:', 'Complete', 1, 50) 
                    break
                elif int(offset_port)-int(min_port) < 100: 
                    #print("[elif문의 elif문] int(offset_port)-int(min_port)")
                    cmd = "sudo proxychains nmap -sS -PN -n -sV -r -T5 -p {}-{} --scan-delay 1 {}".format(min_port, offset_port, ip) # 65435
                    threads.append(cmd)
                    printProgress(idx, len(dataset), 'Progress:', 'Complete', 1, 50) 
                    break
                else:
                    #print("[elif문의 else문]")
                    cmd = "sudo proxychains nmap -sS -PN -n -sV -r -T5 -p {}-{} --scan-delay 1 {}".format(min_port, min_port+99, ip) # 65435
                    threads.append(cmd)
                    continue
            else: 
                print("[else문]")
                continue                 
    
    processing_thread=[]
    num_queue=0
    #init including handler for Thread processing
    for q_cmd in threads:
        #print("[+] start cmd: {}".format(str(q_cmd)))
        num_queue=int(num_queue)+1
        #_handler = "_handler{}".format(str(num_queue))
        _handler = threading.Thread(target=processing(ip, min_port, offset_port, args.o, str(q_cmd), startTime, gettime))
        _handler.start()
    print("[+] Plz wait process")
    printProgress(1, len(threads), 'Progress:', 'Complete', 1, 50)
        #processing_thread.append(_handler)
    #display_offset=len(processing_thread)
    '''
    for t_result in processing_thread:
        t_result.join()
        printProgress(1, display_offset, 'Progress:', 'Complete', 1, 50)
    '''        


"""
10.0.0.0~10.255.255.255
172.16.0.0~172.31.255.255
192.168.0.0~192.168.255.255
------------------------
python3 scan_tool2.py -spt 1 -dpt 65535 -o res -ds domain

        >>test
            proxychains nmap -sS -PN -n -sV --max-rate 32 --max-rtt-timeout 1 -r -T5 -p 1-1023 --scan-delay 0 13.124.22.142
            #sudo tcpdump -i eth0 dst 13.124.22.142
            #proxychains nmap -sS -PN -n -sV --max-rate 32 --max-rtt-timeout 1 -r -T5 -p 1-800 --scan-delay 1 13.124.22.142
        >>scan
            #sudo proxychains nmap -sS -PN -n -sV -max-rate 32 --max-rtt-timeout 1 -r -T5 -p 1-65535 --scan-delay 3 127.0.0.1
            #cmd="sudo proxychains nmap -sT -PN -n -sV -max-rate 32 --max-rtt-timeout 1 -r -T5 -p {}-{} {}".format(sport, dport, ip)
            #cmd="sudo proxychains nmap -sT -PN -n -sV {} -p {}-{}".format(ip, sport, dport)
            #out, err = p.communicate()
            #print("[***]cmd stdout: {}[***]".format(out))
            #print("[***]cmd stderr: {}[***]".format(err))
            #result=os.popen(cmd).read()
        >>main
            #measure_timeClocks(startTime)
            #print("[-] dataset:{}".format(dataset))
            #print("[-] dataset_args:{}".format(dataset_args))
"""
