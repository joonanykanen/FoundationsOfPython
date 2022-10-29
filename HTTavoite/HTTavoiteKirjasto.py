######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joona Nykänen
# Opiskelijanumero: ******
# Päivämäärä: 13.12.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerusKirjasto.py

import sys
import numpy
import datetime

__version__ = "1.2"

class TIEDOT():
    pvm = str
    optunnus = str
    tehtava = str

class TULOKSET():
    teht = str
    tehtnro = str

def Lue(lista):
    try:
        lista1 = [] # Tilapäislista
        lista.clear()  # Tyhjennetään lista ennen lukua.
        rfile = input("Anna luettavan tiedoston nimi: ")
        luettava = open(rfile, "r", encoding="utf-8")
        luettava.readline()  # Lukee otsikkorivim pois.
        n = 0  # Ilmoittaa rivimäärän.
        for rivi in luettava:
            n = n + 1
            rivi = rivi.strip()
            lista1 = rivi.split(';')
            data = TIEDOT()
            data.pvm = datetime.datetime.strptime(lista1[0], "%d-%m-%Y %H:%M:%S")
            data.optunnus = lista1[1]
            data.tehtava = lista1[2]
            lista.append(data)
        print(f"Tiedostosta '{rfile}' luettiin listaan {n} datarivin tiedot." + '\n')
        luettava.close()
        lista1.clear()
        print("Anna uusi valinta.")
    except Exception:
        print(f"Tiedoston '{rfile}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista

def Analyysi(lista, analyysi):
    lista2 = []
    lista3 = []
    analyysi.clear()

    for data in lista:  # Ajetaan tehtäväkohtainen lista.
        lista2.append(data.tehtava)
        
    alkio = lista2[0]
    k = 0  # Laskee eri tehtävien lm.
    tn = 0  # Tehtäväkohtainen numero.
    n = 0  # Rivi-indikaattori

    for rivi in lista2:  # Lasketaan tehtäväkohtainen data listaan.
        n = n + 1
        if alkio != rivi:
            tulos = TULOKSET()
            tulos.teht = alkio
            tulos.tehtnro = tn
            lista3.append(tulos)
            alkio = rivi
            k = k + 1
            tn = 0
        if n == len(lista2):
            tulos = TULOKSET()
            tulos.teht = (lista2[n-1])
            tulos.tehtnro = tn + 1
            lista3.append(tulos)
            k = k + 1
        else:
            tn = tn + 1

    for rivi in lista3:  # Ääriarvovertailun pohjatiedot
        suurin = rivi.tehtnro
        pienin = rivi.tehtnro
        suurinteht = rivi.teht
        pieninteht = rivi.teht
        break

    for rivi in lista3:  
        if rivi.tehtnro > suurin: # Suuremmuusvertailu.
            suurin = rivi.tehtnro
            suurinteht = rivi.teht
        if rivi.tehtnro < pienin: # Pienemmyysvertailu.
            pienin = rivi.tehtnro
            pieninteht = rivi.teht

    # Viimeistelty analyysi
    analyysi.append(f"Palautuksia tuli yhteensä {len(lista2)}, {k} eri tehtävään.")
    analyysi.append(f"Viikkotehtäviin tuli keskimäärin {int(len(lista2) / k)} palautusta.")
    analyysi.append(f"Eniten palautuksia, {suurin}, tuli viikkotehtävään {suurinteht}.")
    analyysi.append(f"Vähiten palautuksia, {pienin}, tuli viikkotehtävään {pieninteht}.")
    analyysi.append("")
    analyysi.append("Tehtävä;Lukumäärä")
    for rivi in lista3:
        analyysi.append(f"{rivi.teht};{rivi.tehtnro}")

    print(f"Analysoitu {len(lista2)} palautusta {k} eri tehtävään.")
    print("Tilastotiedot analysoitu." + '\n')
    lista2.clear()
    lista3.clear()
    print("Anna uusi valinta.")
    return analyysi

def Tallenna(analyysi):
    try:
        wfile = input("Anna kirjoitettavan tiedoston nimi: ")
        kirjoitettava = open(wfile, "w", encoding="utf-8")
        for rivi in analyysi:
            kirjoitettava.write(rivi + '\n')
            print(rivi)
        kirjoitettava.close()
        print(f"Tulokset tallennettu tiedostoon '{wfile}'." + '\n')
        print("Anna uusi valinta.")
    except Exception:
        print(f"Tiedoston '{wfile}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def Palautus(lista, opiskelijat, tehtavat):
    for data in lista: # Laskee opiskelijakohtaisen palautusmäärän
        if data.optunnus not in opiskelijat:
            opiskelijat[data.optunnus] = 1
        else:
            opiskelijat[data.optunnus] += 1
    for i in range(0,61):
        tehtavat[i] = 0
    for n in opiskelijat.values():
        tehtavat[n] += 1
    print("Tehtäväkohtaiset pisteet analysoitu.")
    TallennaPalautus(tehtavat)  # Tallennuskutsu
    opiskelijat.clear()
    tehtavat.clear()
    return None

def Tunti(lista, tuntimatriisi, VIIKKOJA, TUNTEJA):
    for data in lista:
        VIIKKO = int(data.tehtava[1:3])
        TUNTI = int(data.pvm.strftime("%H"))
        tuntimatriisi[VIIKKO - 1][TUNTI] += 1
    print("Tuntikohtaiset palautukset analysoitu.")
    TallennaTunti(tuntimatriisi, VIIKKOJA, TUNTEJA)
    return None

def Aika(lista, viikkomatriisi, VIIKKOJA, PAIVIA):
    for data in lista:
        VIIKKO = int(data.tehtava[1:3])
        PALAIKA = data.pvm
        ALKAIKA = datetime.datetime.strptime('01.09.2020 06:00:00', "%d.%m.%Y %H:%M:%S")
        AIKAERO = PALAIKA - ALKAIKA
        if VIIKKO == 7: # Poikkeustilanne
            PAIVA = int(int(AIKAERO.days) / 2 % 7)
        else:
            PAIVA = int(AIKAERO.days) % 7
        viikkomatriisi[VIIKKO - 1][PAIVA] += 1
    print("Aikavälikohtaiset palautukset analysoitu.")
    TallennaAika(viikkomatriisi, VIIKKOJA, PAIVIA, ALKAIKA)
    return None

def TallennaPalautus(tehtavat):
    try:
        wfile = input("Anna kirjoitettavan tiedoston nimi: ")
        kirjoitettava = open(wfile, "w", encoding="utf-8")
        kirjoitettava.write("Pistemäärä;Opiskelijoita" + '\n')
        for teht, maar in tehtavat.items():
            kirjoitettava.write(f"{teht};{maar}" + '\n')
        kirjoitettava.close()
        print(f"Tulokset tallennettu tiedostoon '{wfile}'." + '\n')
        print("Anna uusi valinta.")
    except Exception:
        print(f"Tiedoston '{wfile}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def TallennaTunti(tuntimatriisi, VIIKKOJA, TUNTEJA):
    try:
        wfile = input("Anna kirjoitettavan tiedoston nimi: ")
        kirjoitettava = open(wfile, "w", encoding="utf-8")
        kirjoitettava.write("Tunti;")
        for tunti in range(TUNTEJA):
            if tunti == (TUNTEJA - 1):
                kirjoitettava.write(f"{TUNTEJA-1}" + '\n')
            else:
                kirjoitettava.write(f"{tunti};")
        for viikko in range(1, (VIIKKOJA + 1)):
            kirjoitettava.write(f"Vko {viikko};")
            for tunti in range(1, (TUNTEJA + 1)):
                if tunti == TUNTEJA:
                    kirjoitettava.write(f"{tuntimatriisi[viikko - 1][tunti - 1]}" + '\n')
                else:
                    kirjoitettava.write(f"{tuntimatriisi[viikko - 1][tunti - 1]};")
        kirjoitettava.close()
        print(f"Tulokset tallennettu tiedostoon '{wfile}'." + '\n')
        print("Anna uusi valinta.")
    except Exception:
        print(f"Tiedoston '{wfile}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def TallennaAika(viikkomatriisi, VIIKKOJA, PAIVIA, ALKAIKA):
    try:
        wfile = input("Anna kirjoitettavan tiedoston nimi: ")
        kirjoitettava = open(wfile, "w", encoding="utf-8")
        kirjoitettava.write("Aikaväli;")
        for paiva in range(PAIVIA):
            if paiva == (PAIVIA - 1):
                kirjoitettava.write(f'{ALKAIKA.strftime("%a %H:%M")}' + '\n')
            else:
                kirjoitettava.write(f'{ALKAIKA.strftime("%a %H:%M")};')
                ALKAIKA = ALKAIKA + datetime.timedelta(days = 1)
        for viikko in range(1, (VIIKKOJA + 1)):
            kirjoitettava.write(f"Vko {viikko};")
            for paiva in range(PAIVIA):
                if paiva == (PAIVIA - 1):
                    kirjoitettava.write(f"{viikkomatriisi[viikko - 1][paiva]}" + '\n')
                else:
                    kirjoitettava.write(f"{viikkomatriisi[viikko - 1][paiva]};")
        kirjoitettava.close()
        print(f"Tulokset tallennettu tiedostoon '{wfile}'." + '\n')
        print("Anna uusi valinta.")
    except Exception:
        print(f"Tiedoston '{wfile}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

#eof
