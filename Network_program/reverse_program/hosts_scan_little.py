#-*- coding: utf-8 -*-
#pip install netaddr pyping
#스캔할 아이피대역 : 192.168.25.0 ~ 192.168.25.255
#파일 경로 C:\Users\namki\AppData\Local\Programs\Python\Python36\Lib\site-packages
import netaddr, pyping
iplist = '172.30.1.1/24'
print('start scan')
def ip_scan(ip):
        try:
                #IP가 살아있는지 확인하자.
                if not pyping.ping(str(ip)).ret_code:
                        #threadLock.acquire()
                        print("Alive Host : {}".format(ip))
                        #threadLock.release()
        except:
                pass
for ip in netaddr.IPNetwork(iplist):
        ip_scan(ip)
        #th = threading.Thread(target=ip_scan(str(ip)), args=str(ip))
        #ping을 날리고 ret_code를 통해 값을 본다(성공은 0이고 실패는 1)
        #threads.append(th)
        #th.start()
                
print("end")
