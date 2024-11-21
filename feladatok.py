from stadionok import Stadionok
from datetime import datetime
#1. Összesen hány stadion van New Yorkban?
#2. Mennyi az összes csapatszám? 
#3. listázd ki azokat a stadionokat, amelyekben  1900.01.01 előtt volt az első mérkőzésük!
#4. Hány olyan stadion van, amelyben 2000 óta nem volt mérkőzés?
#5. Összesen hány csapat játszott Buffalo - ban?

def feladat1(stadionok):
    stadion_szam:int=0
    for i in range (0, len(stadionok), 1):
        if ((stadionok[i].varos) == "New York"):
            stadion_szam += 1
    return stadion_szam

def feladat2(stadionok):
    index_csapat:int=0
    csapatszam:int = 0
    for i in range(0, len(stadionok), 1):
        index_csapat = stadionok[i].csapatok_szama
        if (index_csapat > 0):
            csapatszam += index_csapat
    return csapatszam

def feladat3(stadionok):
    stadionos_lista=[]
    for i in range(0, len(stadionok), 1):
        if (stadionok[i].elso_merk < datetime.strptime("1900-01-01", "%Y-%m-%d")):
            stadionnev:str = stadionok[i].nev
            stadionos_lista.append(stadionnev)
    return stadionos_lista

def feladat4(stadionok):
    ketezres:int=0
    for i in range(0, len(stadionok), 1):
        if (stadionok[i].utolso_merk < datetime.strptime("2000-01-01", "%Y-%m-%d")):
            ketezres += 1
    return ketezres

def feladat5(stadionok):
    buffalocsapat:int=0
    for i in range(0, len(stadionok), 1):
        varos = stadionok[i].varos
        if (varos == "Buffalo"):
            csapatok = stadionok[i].csapatok_szama
            buffalocsapat += csapatok
    return buffalocsapat

