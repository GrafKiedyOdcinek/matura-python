def szyfruj(tekst_jawny, klucz):
    szyfrogram = ""
    dlugosc_klucza = len(klucz)
    for i in range(len(tekst_jawny)):
        kod_tekstu = ord(tekst_jawny[i])
        kod_klucza = ord(klucz[i % dlugosc_klucza])
        nowy_kod = kod_tekstu + (kod_klucza - 64)
        if nowy_kod > 90:
            nowy_kod -= 26
        szyfrogram += chr(nowy_kod)
    return szyfrogram


plik1 = open("tj.txt")
dane1 = plik1.readlines()
plik1.close()
plik2 = open("klucze1.txt")
dane2 = plik2.readlines()
plik2.close()

print("Zadanie 4a")
for tekst_jawny, klucz in zip(dane1, dane2):
    tekst_jawny = tekst_jawny.strip()
    klucz = klucz.strip()
    szyfrogram = szyfruj(tekst_jawny, klucz)
    print(szyfrogram)

def deszyfruj(szyfrogram, klucz):
    tekst_jawny = ""
    dlugosc_klucza = len(klucz)
    for i in range(len(szyfrogram)):
        kod_szyfrogramu = ord(szyfrogram[i])
        kod_klucza = ord(klucz[i % dlugosc_klucza])
        nowy_kod = kod_szyfrogramu - (kod_klucza - 64)
        if nowy_kod < 65:
            nowy_kod += 26
        tekst_jawny += chr(nowy_kod)
    return tekst_jawny

plik3 = open("sz.txt")
dane3 = plik3.readlines()
plik3.close()
plik4 = open("klucze2.txt")
dane4 = plik4.readlines()
plik4.close()

print("Zadanie 4b")
for szyfrogram, klucz in zip(dane3, dane4):
    szyfrogram = szyfrogram.strip()
    klucz = klucz.strip()
    tekst_jawny = deszyfruj(szyfrogram, klucz)
    print(tekst_jawny)
