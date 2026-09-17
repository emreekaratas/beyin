@echo off
set "PATH=%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%APPDATA%\npm;%PATH%"
cd /d "C:\Users\emrek\OneDrive\Masaüstü\apps\beyin"
python tools\watcher.py >> daily\vardiya.log 2>&1