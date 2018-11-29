@echo off
color 0a
mode 200
title  wifi infomation by noski
cls

:YES
echo "wifi list를 확인하시겠습니까?"
set /p select=(Y/N):
if "%select%"=="N" exit
rem md C:\ProgramData\info.txt
netsh wlan show profiles name=* > "C:\ProgramData\info.txt"
find "SSID 이름" "C:\ProgramData\info.txt"
::
set /p wifiname=검색할 와이파이 이름:
::
netsh wlan show profiles name=%wifiname% key=clear > "C:\ProgramData\info.txt"
::
echo "==========confirm=========="
find "키 콘텐츠" "C:\ProgramData\info.txt"
::
if "%wifiname%"=="0" exit
goto YES