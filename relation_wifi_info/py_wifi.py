#-*- coding: utf-8 -*-
#referrer : https://soooprmx.com/archives/5932
import subprocess,sys
#print(sys.stdin.encoding)
#print(sys.stdout.encoding)
try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp949').split('\n')    
    profiles = [i.split(":")[1][1:-1] for i in data if "모든 사용자 프로필" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp949').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "키 콘텐츠" in b]
        try:
            print("{:<20}| {:<}".format(i, results[0]))
        except IndexError:
            print("{:<20}| {:<}".format(i, "password : X"))
        
except UnicodeDecodeError:
    print ("profiles")
    
