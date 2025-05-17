plik = open("dane4.txt")
dane = plik.readlines()
plik.close()


def czy_pierwsza(i):
    if i < 2:
        return False
    for ii in range(2, i):
        if i % ii == 0:
            return False
    else:
        return True


licznik = 0
najwieksza = 0
najmniejsza = 30001
for i in dane:
    if czy_pierwsza(int(i)) == True:
        licznik += 1
    if czy_pierwsza(int(i)) == True and int(i) < najmniejsza:
        najmniejsza = int(i)
    if czy_pierwsza(int(i)) == True and int(i) > najwieksza:
        najwieksza = int(i)
print("Zadanie 6.1")
print(licznik)
print("Zadanie 6.2")
print("Największa", najwieksza)
print("Najmniejsza", najmniejsza)

licznik2 = 0
for i in range(len(dane)-1):
    if int(dane[i]) - 2 == int(dane[i + 1]) and czy_pierwsza(int(dane[i])) == True and czy_pierwsza(int(dane[i + 1])) == True or int(dane[i]) + 2 == int(dane[i + 1]) and czy_pierwsza(int(dane[i])) == True and czy_pierwsza(int(dane[i + 1])) == True:
        licznik2 += 1
print("Zadanie 6.3")
print(licznik2, "pary")
for i in range(len(dane)-1):
    if int(dane[i]) - 2 == int(dane[i + 1]) and czy_pierwsza(int(dane[i])) == True and czy_pierwsza(int(dane[i + 1])) == True or int(dane[i]) + 2 == int(dane[i + 1]) and czy_pierwsza(int(dane[i])) == True and czy_pierwsza(int(dane[i + 1])) == True:
        print(int(dane[i]), int(dane[i+1]))
