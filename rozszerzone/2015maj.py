plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

licznik = 0
licznik2 = 0
licznik8 = 0
for i in dane:
    i = i.strip()
    if i.count("0") > i.count("1"):
        licznik += 1
    if int(i, 2) % 2 == 0:
        licznik2 += 1
    if int(i, 2) % 8 == 0:
        licznik8 += 1
print("Zadanie 4.1")
print(licznik)
print("Zadanie 4.2")
print(licznik2)
print(licznik8)

min = float('inf')
maks = 0
licznik1 = 0
for i in dane:
    i = i.strip()
    i = int(i, 2)
    if i < min:
        min = i
    if i > maks:
        maks = i


def pozycja(a):
    pozycja = 0
    for i in dane:
        i = i.strip()
        i = int(i, 2)
        pozycja += 1
        if a == i:
            return pozycja


print("Zadanie 4.3")
print(pozycja(min))
print(pozycja(maks))
