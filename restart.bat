@echo off

taskkill /F /IM explorer.exe
taskkill /F /IM appname.exe
timeout /t 5 /nobreak

cd ROADEAPP
start appname.exe

timeout /t 5 /nobreak
wmic process where name='appname.exe' CALL setpriority 'realtime'

timeout /t 5 /nobreak
exit