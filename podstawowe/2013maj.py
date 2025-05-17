plik = open("napisy.txt")
dane = plik.readlines()
plik.close()

licznik = 0
for d in dane:
    d = d.strip()
    if len(d) % 2 == 0:
        licznik += 1
print("Zadanie 4a")
print(licznik)

licznik2 = 0
for d in dane:
    d = d.strip()
    ileZer = d.count("0")
    ileJedynek = d.count("1")
    if ileZer == ileJedynek:
        licznik2 += 1
print("Zadanie 4b")
print(licznik2)

sameJedynki = 0
sameZera = 0
for d in dane:
    d = d.strip()
    if d.count("0") == len(d):
        sameZera += 1
    if d.count("1") == len(d):
        sameJedynki += 1
print("Zadanie 4c")
print(sameZera)
print(sameJedynki)

ilosci = dict()
for i in range(2, 17):
    ilosci[i] = 0
for napis in dane:
    napis = napis.strip()
    dlug = len(napis)
    ilosci[dlug] += 1
print("Zadanie 4d")
print(ilosci)
