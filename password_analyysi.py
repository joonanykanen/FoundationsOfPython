###############################
# Tekijä: Joona Nykänen
# Päivämäärä: 20.12.2021
# Kaikki oikeudet pidätetään.
###############################

import sys
import string
import secrets

# Kiintoarvot
TESTIAJOT = 10000

def Analyysi(lista, analyysi):
    read = input("Haluatko tulostaa analyysin taustaprosessin? (K/e): ")
    print("Suoritetaan analyysiä, odota hetki.")
    if read != "K" and read != "k" and read != "":
        print("Huom! Analyysi voi kestää tietokoneen laskentatehosta riippuen jopa minuutin.")
    alphabet = string.ascii_letters + string.digits

    # Analyysin toistorakenne
    for MERKIT in range(5, 101):
        for i in range(0, TESTIAJOT):
            n = 0
            while True:
                n = n + 1
                password = ''.join(secrets.choice(alphabet) for i in range(MERKIT))
                # Kriteerit (1 iso kirjain, 1 pieni kirjain sekä vähintään 3 numeroa)
                if (any(c.islower() for c in password)
                        and any(c.isupper() for c in password)
                        and sum(c.isdigit() for c in password) >= 3):
                    break
            lista.append(n)
        yht = 0
        for i in lista:
            yht = yht + int(i)
        ka = yht / len(lista)
        analyysi.append(f"{MERKIT};{ka:.6f}")
        if read == "K" or read == "k" or read == "":
            print(f"{MERKIT} merkkisen salasanan tekemiseen meni keskimäärin {ka:.6f} kertaa.")

    print("Analyysi suoritettu.")
    return analyysi

def Tallenna(analyysi):
    try:
        rfile = input("Minkä nimiseen tiedostoon haluat tallentaa?: ")
        kirjoitus = open(rfile, "w", encoding="utf-8")
        kirjoitus.write("Pituus;Keskiarvo" + '\n')
        for rivi in analyysi:
            kirjoitus.write(rivi + '\n')
        kirjoitus.close()
        print(f"Tallentaminen onnistui tiedostoon {rfile}." + '\n')
    except Exception:
        print("Jokin meni vikaan tallennuksessa, lopetetaan.")
        sys.exit(0)
    return None

def Paaohjelma():
    lista = []
    analyysi = []
    print("Tämä ohjelma laskee keskimääräisen (5-100)-merkkisen salasanan tekemiseen")
    print("tietokoneen käyttämät silmukat ja tallentaa analyysitiedot haluamaasi tiedostoon." + '\n')
    print("Salasanan turvallisuuskriteerit:")
    print("Salasanassa on oltava väh. 1 iso kirjain, väh. 1 pieni kirjain sekä väh. 3 numeroa." + '\n')
    read = input("Haluatko suorittaa analyysin? (K/e): " + '\n')
    if read == "K" or read == "k" or read == "":
        analyysi = Analyysi(lista, analyysi)
        Tallenna(analyysi)
    else:
        print("Poistutaan ohjelmasta.")
    print("Kiitos ohjelman käytöstä.")
    return None

Paaohjelma()

#eof
