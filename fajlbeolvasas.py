from stadionok import Stadionok

def beolvas(fajlnev:str="", stadionok_lista=[]):
    fajlom = open(fajlnev, "r", encoding="UTF-8")
    elso_sor = fajlom.readline()
    tobbi_sor_lista = fajlom.readlines()
    print(tobbi_sor_lista)
    """feldolgozzuk a listát"""
    """splitteljük a lista sorait"""
    for i in range(0, len(tobbi_sor_lista), 1):
            sor = tobbi_sor_lista[i].strip()
            sor_lista=sor.split(";")
            print(sor_lista)
            stadion = Stadionok(sor_lista[0], sor_lista[1], sor_lista[2], sor_lista[3], sor_lista[4])
            stadionok_lista.append(stadion)
    fajlom.close()
    return stadionok_lista

