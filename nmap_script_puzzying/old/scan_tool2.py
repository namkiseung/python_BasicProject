import argparse,os, time, datetime
import sys,subprocess

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

def processing(ip,sport,dport,fname,startTime,gettime):
    #Port-Scanning (1)input datas (2)exec cmd (3) make output-files (4) display processbar (5) record time
    try:
        #proxychains nmap -sT -PN -n -sV -max-rate 32 --max-rtt-timeout 1 -r -T5 -p 1-65535 127.0.0.1
        cmd="proxychains nmap -sT -PN -n -sV -max-rate 32 --max-rtt-timeout 1 -r -T1 -p {}-{} --scan-delay 1 --max-scan-delay 30 --host-timeout 20ms {}".format(sport, dport, ip)
        print("[*] cmd : {}".format(cmd))
        #cmd="proxychains nmap -sT -PN -n -sV -max-rate 32 --max-rtt-timeout 1 -r -T5 -p {}-{} {}".format(sport, dport, ip)
        p = subprocess.Popen(cmd, shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
        #out, err = p.communicate()
        #print("[***]cmd stdout: {}[***]".format(out))
        #print("[***]cmd stderr: {}[***]".format(err))
        result=list()
        for line in p.stdout.readlines():
            result.append(line.decode('euc-kr'))
        print(result)
            #retval = p.wait()
        #cmd="proxychains nmap -sT -PN -n -sV {} -p {}-{}".format(ip, sport, dport)
        #result=os.popen(cmd).read()
        fname="{}-{}-{}".format(fname, ip, gettime)
        os.popen("touch ./log_scandata/9000784/{}.txt".format(fname)).read()
        files = open("./log_scandata/9000784/{}.txt".format(fname),"w")
        result = result.split("'")
        for x in result:
            files.write("{}".format(x))
        files.close()
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
    args=argv_conf()
    startTime = time.time()
    gettime=datetime.datetime.today().strftime("%H%M-%S-%y%m%d")
    print(gettime)
    #dataset에서 1개 IP 나올떄 마다 function called name of the processing 
    #call single ip
    #processing(args.ip, args.spt, args.dpt, args.o, startTime, gettime)
    #call multi ip inside dataset
    idx=0
    dataset_args=args.ds
    #print("[-] dataset_args:{}".format(dataset_args))
    dataset=dataset_url(dataset_args)
    #print("[-] dataset:{}".format(dataset))
    for ip in dataset:
        idx=idx+1
        print("[*] count: {} | ip: {}".format(idx, ip))
        processing(ip, args.spt, args.dpt, args.o, startTime, gettime)
        printProgress(idx, len(dataset), 'Progress:', 'Complete', 1, 50)
    #measure_timeClocks(startTime)

