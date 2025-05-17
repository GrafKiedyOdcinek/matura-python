import math

plik = open("punkty.txt")
dane = plik.readlines()
plik.close()


def isprime(l):
    if l < 2:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    else:
        return True


licznik1 = 0
for i in dane:
    i = i[:-1]
    if isprime(int(i.split(" ")[0])) == True and isprime(int(i.split(" ")[1])) == True:
        licznik1 += 1
print("Zadanie 4.1")
print(licznik1)

def cyfropodobne(a, b):
    c = []
    d = []
    e = []
    f = []
    for i in str(a):
        c.append(i)
    for i in str(b):
        d.append(i)
    c.sort()
    d.sort()
    for i in c:
        if i not in e:
            e.append(i)
    for i in d:
        if i not in f:
            f.append(i)
    if e == f:
        return True


licznik2 = 0
for i in dane:
    i = i[:-1]
    if cyfropodobne(str(i.split(" ")[0]), str(i.split(" ")[1])) == True:
        licznik2 += 1
print("Zadanie 4.2")
print(licznik2)

maks = 0
m = []
for i in dane:
    i = i[:-1]
    for ii in dane:
        ii = ii[:-1]
        dlugosc = math.sqrt((int(ii.split(" ")[0]) - int(i.split(" ")[0])) ** 2 + (int(ii.split(" ")[1]) - int(i.split(" ")[1])) ** 2)
        if dlugosc > maks:
            maks = dlugosc
            m.append([i.split(" ")[0], i.split(" ")[1], ii.split(" ")[0], ii.split(" ")[1]])
print("Zadanie 4.3")
print("x1:", m[-1][0], "y1:", m[-1][1], "x2:", m[-1][2], "y2:", m[-1][3])
print(round(maks))

licznikA = 0
licznikB = 0
licznikC = 0
for i in dane:
    i = i[:-1]
    if -5000 < int(i.split(" ")[0]) < 5000 > int(i.split(" ")[1]) > -5000:
        licznikA += 1
    elif -5000 == int(i.split(" ")[0]) or int(i.split(" ")[0]) == 5000 or 5000 == int(i.split(" ")[1]) or int(i.split(" ")[1]) == -5000:
        licznikB += 1
    else:
        licznikC += 1
print("Zadanie 4.4")
print(licznikA)
print(licznikB)
print(licznikC)
