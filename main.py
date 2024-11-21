from stadionok import Stadionok
import fajlbeolvasas
import feladatok

stadionok = fajlbeolvasas.beolvas("stadionok.txt",[])
'''print(stadionok)
for i in range(0, len(stadionok), 1):
    print(stadionok[i])
print(f"Első stadion neve: {stadionok[i]}")'''

stadion_szam = feladatok.feladat1(stadionok)
print(f"New York-ban {stadion_szam} stadion van.")

csapatszam = feladatok.feladat2(stadionok)
print(f"Az összes csapatszám: {csapatszam}")

stadionos_lista = feladatok.feladat3(stadionok)
print(f"Ezekben a stadionokban volt 1900.01.01 előtt mérkőzés: {stadionos_lista}")

ketezres = feladatok.feladat4(stadionok)
print(f"Ennyi stadionban nem volt 2000-óta mérkőzés: {ketezres}")

buffalocsapat = feladatok.feladat5(stadionok)
print(f"Összesen {buffalocsapat} játszott Buffalo-ban!")