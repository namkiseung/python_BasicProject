import os, subprocess, sys, time
import pytube

def __convert():
    new_filename=input("[+]변환할 확장자는?")
    default_filename = vids[vnum].default_filename
    subprocess.call(['ffmpeg', '-i',
                 os.path.join(parent_dir, default_filename),
                 os.path.join(parent_dir, new_filename)
                 ])
    pass

try:
    yt=pytube.YouTube(input("download URL : "))
    vids = yt.streams.all()
except:
    print("[+]저작권에 의해 다운로드가 막힌 영상입니다.")
    quit()
        
for i in range(len(vids)):
    print("번호 : [",i, '] '+'확장자 및 화질: {}'.format(str(vids[i])[str(vids[i]).find("mime_type=\""):str(vids[i]).find("fps")]))

vnum= int(input("화질 번호 입력 : "))
try:
    print("[+] Loding....")
    vids[vnum].download(os.getcwd().replace("\\","/"))
except PermissionError:
    print("[+]권한이 없습니다.")
    quit()

print("[+]영상 다운로드 완료 (설치된 영상 경로 : {})".format(os.getcwd().replace("\\","/")))
