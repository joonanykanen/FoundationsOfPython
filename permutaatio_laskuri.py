###############################
# Tekijä: Joona Nykänen
# Päivämäärä: 21.12.2021
# Kaikki oikeudet pidätetään.
###############################

from itertools import combinations
from math import comb
import time


def Valikko():
    print("Valitse yksi vaihtoehdoista (0-2).")
    print("1) Syötä luvut")
    print("2) Laske kombinaatio")
    print("0) Lopeta")
    while (True):
        valinta = input("Valintasi: ")
        if valinta == "0" or valinta == "1" or valinta == "2":
            print()
            break
        else:
            print("Syötä valintasi kokonaislukuna (0-2)." + '\n')
    return valinta

def Luvut(luvut):
    luvut.clear()
    while (True):
        luku = input("Syötä summattavia lukuja järjestyksessä (n1 n2 n3.. ..nm): ")
        luvut = luku.split(' ')
        if len(luvut) < 2:
            print("Lukuja on oltava vähintään 2 kpl." + '\n')
        else:
            break
    while (True):
        summa = input("Syötä nyt edellisistä luvuista muodostuva summa: ")
        summatarkastus = Summatarkistus(luvut, summa)
        if summatarkastus == False:
            print("Lukujen yhteissumma on pienempi kuin määrätty summa, yritä uudelleen." + '\n')
        else:
            luvut.append(summa)
            break
    while (True):
        summakpl = input("Syötä lopuksi summattavien lukujen määrä: ")
        if int(summakpl) > len(luvut) - 1:
            print("Summattavia lukuja ei voi olla enemmän kuin käyttäjän syötteessä.")
            print("Yritä uudelleen." + '\n')
        else:
            luvut.append(summakpl)
            break
    print('\n' + f"Luvut syötetty listaan. Summattavia lukuja yht. {len(luvut) - 2} kpl." + '\n')
    return luvut

def Analyysi(luvut, analyysi):
    analyysi.clear()
    summakpl = int(luvut.pop())
    summa = int(luvut.pop())
    if comb(len(luvut), summakpl) > (10 ** 5):
        print("Kombinaatioiden määrä ylittyy, valitse pienempi otos.")
        return None
    # Tässä vaiheessa listasta on poimittu oleelliset tiedot
    # ja se sisältää jäljelle jääneet yhteenlaskettavat luvut.
    kombinaatiot = combinations(luvut, summakpl)

    start_time = time.time() # Ajastin (start)

    for i in list(kombinaatiot):
        yht = 0
        for n in range(summakpl):
            yht = yht + int(i[n])
            analyysi.append(int(i[n]))
        if yht == summa:
            print("Kombinaatio löytyi.")
            print(f"{analyysi} yhdessä laskettuna on {summa}." + '\n')
            break
        else:
            analyysi.clear()
    if len(analyysi) == 0:
        print("Kombinaatioita ei löytynyt.")

    aikaero = time.time() - start_time # Ajastin (stop)
    print(f"--- Suoritus kesti {aikaero:.2f} sekuntia ---" + '\n')
    return None

def Summatarkistus(luvut, summa):
    yht = 0
    for luku in luvut:
        yht = yht + int(luku)
    if yht < int(summa):
        return False
    else:
        return True

def Paaohjelma():
    print("Tämä ohjelma laskee määritetyn summan annetuilla luvuilla.")
    luvut = []
    analyysi = []
    while (True):
        valinta = Valikko()
        if valinta == "1":
            luvut = Luvut(luvut)
        elif valinta == "2":
            if len(luvut) == 0:
                print("Lue luvut ennen laskemista." + '\n')
            else:
                Analyysi(luvut, analyysi)
        elif valinta == "0":
            print("Lopetetaan.")
            luvut.clear()
            break
    print("Kiitos ohjelman käytöstä.")
    return None

Paaohjelma()

#eof