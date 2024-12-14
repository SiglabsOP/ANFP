@echo off

REM Kill any running instances of python.exe try  taskkill /f /im py.exe or taskkill /f /im python.exe /fi "WINDOWTITLE eq errorhandler.py"
 
REM Run the Python script                           // you can change these paths
REM Run the Python scripts simultaneously
start "" "C:\Users\grhlu\AppData\Local\Programs\Python\Python312\python.exe" "C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\updater.py"
start "" "C:\Users\grhlu\AppData\Local\Programs\Python\Python312\python.exe" "C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\errorhandler.py"
start "" "C:\Users\grhlu\AppData\Local\Programs\Python\Python312\python.exe" "C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\parser\reminders.py"