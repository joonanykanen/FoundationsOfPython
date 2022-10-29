from itertools import permutations
import time

def T4a():
    start_time = time.time()

    perm = permutations([257, 304, 391, 642, 782, 1541, 2184, 2206], 3)

    for i in list(perm):
        if i[0] + i[1] + i[2] == 3223:
            print(f"{i[0]} + {i[1]} + {i[2]} = 3223")
        else:
            continue

    aika = "--- Suoritus kesti  {:.4f} sekuntia ---".format(time.time() - start_time)
    print(aika)
    return None

def T4bi():
    start_time = time.time()

    perm = permutations([177, 337, 354, 365, 493, 573, 651, 691], 4)

    for i in list(perm):
        if i[0] + i[1] + i[2] + i[3] == 2200:
            print(f"{i[0]} + {i[1]} + {i[2]} + {i[3]}= 2200")
        else:
            continue

    aika = "--- Suoritus kesti  {:.4f} sekuntia ---".format(time.time() - start_time)
    print(aika)
    return None

def T4bii():

    start_time = time.time()

    perm = permutations([177, 337, 354, 365, 493, 573, 651, 691], 5)

    for i in list(perm):
        if i[0] + i[1] + i[2] + i[3] + i[4] == 2200:
            print(f"{i[0]} + {i[1]} + {i[2]} + {i[3]} + {i[4]} = 2200")
        else:
            continue
    
    aika = "--- Suoritus kesti  {:.4f} sekuntia ---".format(time.time() - start_time)
    print(aika)
    return None

def Valikko():
    print("T4a (1), T4bi (2), T4bii (3), Lopeta (0)")
    valinta = int(input("Minkä tehtävistä haluat suorittaa? (0-4): "))
    print()
    return valinta

def Paaohjelma():
    while(True):
        valinta = Valikko()
        if valinta == 1:
            T4a()
        elif valinta == 2:
            T4bi()
        elif valinta == 3:
            T4bii()
        elif valinta == 0:
            print("Lopetetaan.")
            break
        else:
            print("Yritä uudestaan.")
        print()
    return None

Paaohjelma()

