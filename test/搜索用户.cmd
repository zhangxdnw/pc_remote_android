@echo off
cd ..
if not exist device.txt (python utils/device_util.py > device.txt)
for /f "tokens=2 delims='" %%i in (device.txt) do set serial=%%i
echo %serial%

python main.py -d %serial% -p com.ss.android.ugc.aweme -a find_user -x {'keyword':'zxd'}

echo %ERRORLEVEL%
pause