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
# Tehtävä HTTavoite.py

import numpy
import HTTavoiteKirjasto

VIIKKOJA = 14 # Kiintoarvot (config)
TUNTEJA = 24
PAIVIA = 7

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("4) Analysoi opiskelijoiden palautusmäärät")
    print("5) Analysoi tuntikohtaiset palautukset")
    print("6) Analysoi aikavälien palautukset")
    print("0) Lopeta")
    while(True):
        try:
            valinta = int(input("Valintasi: "))
            break
        except Exception:
            print("Anna valinta kokonaislukuna.")
    return valinta

def paaohjelma():
    lista = [] # Alustukset ja alkutoimenpiteet
    analyysi = []
    opiskelijat = {}
    tehtavat = {}

    while (True):
        valinta = valikko()
        if valinta == 1:
            lista = HTTavoiteKirjasto.Lue(lista)
        elif valinta == 2:
            if len(lista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä." + '\n')
                print("Anna uusi valinta.")
            else:
                HTTavoiteKirjasto.Analyysi(lista, analyysi)
        elif valinta == 3:
            if len(lista) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta." + '\n')
                print("Anna uusi valinta.")
            else:
                HTTavoiteKirjasto.Tallenna(analyysi)
        elif valinta == 4:
            if len(lista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä." + '\n')
                print("Anna uusi valinta.")
            else:
                HTTavoiteKirjasto.Palautus(lista, opiskelijat, tehtavat)
        elif valinta == 5:
            if len(lista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä." + '\n')
                print("Anna uusi valinta.")
            else:
                tuntimatriisi = numpy.zeros((VIIKKOJA, TUNTEJA), int)
                HTTavoiteKirjasto.Tunti(lista, tuntimatriisi, VIIKKOJA, TUNTEJA)
                numpy.delete(tuntimatriisi, numpy.s_[:], None) # Tuhoaa matriisin käytön jälkeen.
        elif valinta == 6:
            if len(lista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä." + '\n')
                print("Anna uusi valinta.")
            else:
                viikkomatriisi = numpy.zeros((VIIKKOJA, PAIVIA), int)
                HTTavoiteKirjasto.Aika(lista, viikkomatriisi, VIIKKOJA, PAIVIA)
                numpy.delete(viikkomatriisi, numpy.s_[:], None)
        elif valinta == 0:
            lista.clear()
            analyysi.clear()
            opiskelijat.clear()
            tehtavat.clear()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan." + '\n')
            print("Anna uusi valinta.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

#eof
