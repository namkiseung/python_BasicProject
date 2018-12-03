##import subprocess
##
##for i in range(5):
##    address = "192.168.0.{}".format(i)
##    cmd="ping -n 2 -w 100".format(address)
##    try:
##        out = subprocess.check_output.split(cmd)
##        print(out)
##    except Exception as e:
##        pass

count=0
while count<10:
    print count
    count = count+1
