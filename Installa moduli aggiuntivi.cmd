echo off
cls

echo. Work shifts integrator 
echo. Premi un tasto per confermare l'installazione dei moduli aggiuntivi...
pause>nul

py -m pip install -U openpyxl
py -m pip install -U PyQt5
py -m pip install -U PyQt5-stubs

echo.
echo. Premi un tasto per uscire...
pause>nul