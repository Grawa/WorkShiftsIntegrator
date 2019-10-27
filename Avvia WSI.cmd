echo off
cls

if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

echo. Work shifts integrator - Logs:
echo.

py WSI.py

TIMEOUT 10
EXIT