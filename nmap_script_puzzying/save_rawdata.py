import subprocess, os, sys

class Save_raw:
    _data = list()
    _ip=""
    def getData(self):
        return self._data
    def setData(self, data):
        self._data = data
    def setIp(self, ip):
        self._ip=ip

    def sniff(self, ip):
        cmd="sudo tcpdump -i eth0 dst {}".format(ip)
        p = subprocess.Popen(cmd, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        print(p.stdout.readlines())
        pass
#class filtering_test:
#    result=

if __name__=="__main__":
    
    test=list()
    for x in range(1,10):
        if int(x)!=3:
            test.append(x)
    a=Save_raw()
    a.setData(test)
    a.sniff("8.8.8.8")
    print(a._data)
