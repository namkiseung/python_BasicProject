import netaddr
import threading
from pyping import *
from core import *
iplist = '192.168.0.0/24'
threadLock = threading.Lock()
threads = []

print ('Start Scan')
def IPScan(ip):
    try:
        if not ping(str(ip)).ret_code:
            threadLock.acquire()
            print ('Alive Host : ' + str(ip))
            threadLock.release()
    except:
        pass

for ip in netaddr.IPNetwork(iplist):
    ip = str(ip)
    th = threading.Thread(target=IPScan, args=(ip,))
    th.start()
    threads.append(th)

for t in threads:
    t.join()

print ('End Scan.')