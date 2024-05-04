@echo on
chcp 65001

REM @ SCRIPT PARA LIMPEZA E OTIMIZAÇÃO DE OS WINDOWS
REM @
REM @ Versão script_clear_v08 - 18/01/2024
REM @ - Remoção de mais arquivos temporários do Windows, navegadores e cclear, além da otimização e limpeza de disco e rede.

REM ******************** ELIMINANDO CCLEAR ********************
taskkill /F /IM "ccleaner64.exe"
taskkill /F /IM "ccleaner.exe"

REM ******************** FECHAR PROGRAMAS ABERTOS ********************
taskkill /F /FI "USERNAME eq %USERNAME%" /FI "'IMAGENAME' ne explorer.exe" /FI "'IMAGENAME' ne cmd.exe"

REM ******************** PARANDO ATULIZAÇÕES ********************
start /wait net stop wuauserv
start /wait reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoUpdate /t REG_DWORD /d 1 /f

REM ******************** LIXEIRA ********************
del C:\$recycle.bin\* /s /q
PowerShell.exe -NoProfile -Command Clear-RecycleBin -Confirm:$false >$null
del $null

REM ******************** PASTA TEMP DOS USUÁRIOS ********************

REM Apaga todos arquivos da pasta Temp de todos os usuários, mantendo das pastas
for /d %%F in (%USERPROFILE%\*) do del "%%F\AppData\Local\Temp\*" /s /q

REM cria arquivo vazio.txt dentro da pasta Temp de todos usuários
for /d %%F in (%USERPROFILE%\*) do type nul >"%%F\Appdata\Local\Temp\vazio.txt"

REM apaga todas as pastas vazias dentro da pasta Temp de todos usuários (mas não apaga a própria pasta Temp)
for /d %%F in (%USERPROFILE%\*) do robocopy "%%F\AppData\Local\Temp\" "%%F\AppData\Local\Temp\" /s /move /NFL /NDL /NJH /NJS /nc /ns /np

REM Apaga arquivo vazio.txt dentro da pasta Temp de todos usuários
for /d %%F in (%USERPROFILE%\*) do del "%%F\AppData\Local\Temp\vazio.txt"

REM ******************** WINDOWS TEMP ********************

REM Apaga todos arquivos da pasta \Windows\Temp, mantendo das pastas
del C:\Windows\Temp\* /s /q

REM cria arquivo vazio.txt dentro da pasta \Windows\Temp
type nul > C:\Windows\Temp\vazio.txt

REM apaga todas as pastas vazias dentro da pasta \Windows\Temp (mas não apaga a própria pasta)
robocopy C:\Windows\Temp C:\Windows\Temp /s /move /NFL /NDL /NJH /NJS /nc /ns /np

REM Apaga arquivo vazio.txt dentro da pasta \Windows\Temp
del C:\Windows\Temp\vazio.txt

REM ******************** ARQUIVOS DE LOG DO WINDOWS ********************

del C:\Windows\Logs\cbs\*.log
del C:\Windows\ServiceProfiles\LocalService\AppData\Local\Temp\MpCmdRun.log
del C:\Windows\Logs\measuredboot\*.log
del C:\Windows\Logs\MoSetup\*.log
del C:\Windows\Panther\*.log /s /q
del C:\Windows\Performance\WinSAT\winsat.log /s /q
del C:\Windows\inf\*.log /s /q
del C:\Windows\logs\*.log /s /q
del C:\Windows\SoftwareDistribution\*.log /s /q
del C:\Windows\Microsoft.NET\*.log /s /q
for /d %%F in (%USERPROFILE%\*) do del "%%F\AppData\Local\Microsoft\OneDrive\setup\logs\*.log" /s /q

REM ******************** EDGE ********************
taskkill /F /IM "msedge.exe"

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\Cache\Cache_Data\data*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\Cache\Cache_Data\f*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\Cache\Cache_Data\index. /s /q

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\GPUCache\d*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\GPUCache\i*. /s /q

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\IndexedDB\https_ntp.msn.com_0.indexeddb.leveldb\*.* /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\*.pma /s /q

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Code Cache"\js\*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Code Cache"\wasm\*. /s /q

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Platform Notifications"\*.* /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\EdgePushStorageWithWinRt\*.log /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"File System"\*. /s /q


for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Service Worker"\CacheStorage\*. /s /q
for /d %%F in (C:\Users\*) do robocopy %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Service Worker"\CacheStorage\ %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Service Worker"\CacheStorage\ /s /move /NFL /NDL /NJH /NJS /nc /ns /np
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Service Worker"\Database\*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\"Service Worker"\ScriptCache\*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\EdgeCoupons\coupons_data.db\*.ldb /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\EdgeCoupons\coupons_data.db\index. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\Default\EdgeCoupons\coupons_data.db\*.log /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Microsoft\Edge\"User Data"\BrowserMetrics\*.pma /s /q

REM ******************** CHROME ********************
taskkill /F /IM "chrome.exe"

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\Cache\Cache_Data\data*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\Cache\Cache_Data\f*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\Cache\Cache_Data\index. /s /q

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\GPUCache\d*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\GPUCache\i*. /s /q

del C:\Program Files\Google\Chrome\Application\SetupMetrics\*.pma /s /q

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Code Cache"\js\*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Code Cache"\wasm\*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Code Cache"\webui_js\*. /s /q

for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Service Worker"\CacheStorage\*. /s /q
for /d %%F in (C:\Users\*) do robocopy %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Service Worker"\CacheStorage\ %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Service Worker"\CacheStorage\ /s /move /NFL /NDL /NJH /NJS /nc /ns /np
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Service Worker"\Database\*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\Default\"Service Worker"\ScriptCache\*. /s /q
for /d %%F in (C:\Users\*) do del %%F\AppData\Local\Google\Chrome\"User Data"\brow*.* /s /q

REM ******************** OTIMIZAÇÃO DE REDE ********************
netsh int ipv4 set dynamicport tcp start=10000 num=5000

netsh interface tcp set global autotuning=restricted

sc config bits start=disabled
netsh interface ipv6 set global randomizeidentifiers=disabled
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f

netstat -s -p tcp > NUL
netstat -s -p udp > NUL
ipconfig /flushdns
timeout /t 5 /nobreak

REM ******************** OTIMIZAÇÃO DE DISCO ********************
start /wait powercfg /hibernate off
start /wait sfc /scannow
start /wait dism /online /cleanup-image /CheckHealth
start /wait dism /online /cleanup-image /restorehealth
start /wait defrag /C
timeout /t 5 /nobreak

REM ******************** REINICIALIZAÇÃO ********************
echo Ass.: Leonardo Rodrigues - Analista de Suporte - Fictix
echo Version: script_clear_v08
timeout /t 5 /nobreak
start /wait shutdown /r /t 0

