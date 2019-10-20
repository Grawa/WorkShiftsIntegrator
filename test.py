import os
import glob


directory = os.path.dirname("C:\\Users\\USER\\Google Drive\\TimeTuneFolder\\TimeTune Backup (2019-10-01 124721) (ONEPLUS A6010) - Co - Copia - Copia - Copia - Copia - Copia - Copia (5) - Copia")  # seleziona la directory del file selezionato
listafiledir = glob.glob(directory + "\\*")  # elenca in una lista i file presenti nella directory

# ELENCA SOLO I FILE CONTENENTI LA PAROLA CHIAVE "TimeTune Backup" E CHE NON HANNO ESTENSIONE es(.txt)
filestt = []
for filex in listafiledir:
    if os.path.isfile(filex):  # controlla che siano file e non cartelle               # todo tabella.csv non trovato  e se creo una folder su ttfolder non funziona
        print(filex)
        if "TimeTune Backup" in filex:  # controlla che ci sia "TimeTune Backup"
            if not os.path.splitext(filex)[1]:      # controlla che il file non abbia una estensione
                filestt.append(filex)
print(filestt)
file_vecchi = []
file_nuovo = max(filestt, key=os.path.getctime)  # restituisce il piu recente
for file in filestt:                             # rimuove i vecchi file
    if file != file_nuovo:                       # tranne quello piu recente
        file_vecchi.append(file)


