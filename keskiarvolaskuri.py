######################################################################
# Tekijä: Joona Nykänen
# Päivämäärä: 3.7.2022
######################################################################

def keskiarvo():
    yht = 0
    ka = 0
    n = 0
    print("Syötä positiivisia reaalilukuja.\nSyötä 0, kun olet valmis.\n")
    syote = float(input("Luku 1: "))
    while(syote != 0):
        n = n + 1
        yht = yht + syote
        syote = float(input(f"Luku {n+1}: "))
    try:
        ka = yht / n
    except ZeroDivisionError:
        print("\nEt antanut yhtään lukua.")
    return ka

def paaohjelma():
    print("Tämä ohjelma laskee annettujen lukujen keskiarvon.\n")
    ka = keskiarvo()
    if ka > 0:
        print(f"\nAntamiesi lukujen keskiarvo on {ka}.")
    print("Kiitos ohjelman käytöstä.")
    return 0

paaohjelma()