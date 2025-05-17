import math

plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

licznik = 0
suma = 0
for i in dane:
    i = i[:-1]
    i = i.split(" ")
    if int(i[0]) < int(i[1]) < int(i[2]):
        licznik += 1
    suma += math.gcd(int(i[0]), int(i[1]), int(i[2]))
print("Zadanie 4.1")
print(licznik)
print("Zadanie 4.2")
print(suma)

licznik2 = 0
maks = 0
licznik3 = 0
for i in dane:
    suma1 = 0
    i = i.strip()
    i = i.replace(" ", "")
    for ii in range(0, len(i)):
        suma1 += int(i[ii])
    if suma1 == 35:
        licznik2 += 1
    if suma1 > maks:
        maks = suma1

for i in dane:
    suma1 = 0
    i = i.strip()
    i = i.replace(" ", "")
    for ii in range(0, len(i)):
        suma1 += int(i[ii])
    if suma1 == maks:
        licznik3 += 1
print("Zadanie 4.3")
print(licznik2)
print(maks)
print(licznik3)
