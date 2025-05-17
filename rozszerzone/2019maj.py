from math import gcd

plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

licznik = 0
for i in dane:
    i = i[:-1]
    for ii in range(0, 100):
        if 3**ii == int(i):
            licznik += 1
print("Zadanie 4.1")
print(licznik)

print("Zadanie 4.2")
for i in dane:
    a = 1
    b = 0
    i = i[:-1]
    for ii in i:
        for iii in range(1, int(ii)+1):
            a *= iii
        b += a
        a = 1
    if int(i) == b:
        print(i)


def nwdlisty(a):
    nwd = gcd(a[0], a[1])
    for i in range(2, len(a)):
        nwd = gcd(nwd, a[i])
    return nwd


def ciag(c):
    licznik = 0
    for ii in range(0, len(c)):
        if nwdlisty(c) == 1 and len(c) > 2:
            c.pop(-1)
        else:
            licznik += 1
    return licznik, c[0], nwdlisty(c)


c = []
for i in dane:
    i = i[:-1]
    c.append(int(i))
d = []
for i in range(0, len(c)):
    d.append(c.copy())
    c.pop(0)
c = []
for i in dane:
    i = i[:-1]
    c.append(int(i))
maks = 0
e = []
f = []
for i in range(0, len(c)-1):
    if ciag(d[i])[0] > maks:
        maks = ciag(d[i])[0]
        e.append(ciag(d[i])[1])
        f.append(ciag(d[i])[2])
print("Zadanie 4.3")
print(e[-1])
print(maks)
print(f[-1])
