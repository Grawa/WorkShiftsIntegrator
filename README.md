# Work Shifts Integrator
Il programma aggiunge dei turni di lavoro ad un database dell'app (di terze parti) Timetune per Android.
![wsi](https://github.com/Grawa/WorkShiftsIntegrator/blob/master/Immagini/wsi_demo.png)


## Funzionalità:
- Visualizzazione dei turni
- Reminder e note personalizzabili per turno
- Possibilità di disattivare alcuni reminder
- Verifica automatica disponibilità parcheggio
- Verifica errori di scrittura (es. doppi o nuovi turni)

***Funzionalità aggiuntive:***
- Individuazione vecchi database
- Integrazione con google drive per windows
- Comandi SQL manuali per il database

## Installazione
Su windows 10:
1. Installare Python 3.8
2. Avviare "Installa moduli aggiuntivi.cmd"
3. Avviare "Avvia WSI.cmd"

Nota: E' necessario che la cartella AO_files sia nella stessa directory del file AO.py
##
Il programma è testato e funzionante su python 3.7 e 3.8 su windows 10. Richiede solo questi moduli aggiuntivi:
```shell
pip install openpyxl
pip install PyQt5
pip install PyQt5-stubs
```


## Verificato funzionamento fino alla rel. di Timetune v2.9.3 
## Nota: Deve esserci almeno un "evento" già memorizzato sul database per poter scrivere i turni sul DB, altrimenti alla prima scrittura si otterrà un errore.

