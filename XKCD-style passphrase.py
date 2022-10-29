import secrets

# sanalistalle tiedostopolku
POLKU = 'C:\Windows\words'

# sanojen lukumäärä salasanassa
SANAT = 6

with open(POLKU) as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(SANAT))
    print(password)
f.close()
