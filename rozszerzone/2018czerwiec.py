plik1 = open("dane1.txt")
dane1 = plik1.readlines()
plik1.close()
plik2 = open("dane2.txt")
dane2 = plik2.readlines()
plik2.close()

a = []
b = []
licznik1 = 0
for i in dane1:
    i = i[:-1]
    a.append(i.split(" ")[-1])
for i in dane2:
    i = i[:-1]
    b.append(i.split(" ")[-1])
for i in range(0, len(a)):
    if a[i] == b[i]:
        licznik1 += 1
print("Zadanie 4.1")
print(licznik1)

c = []
d = []
licznik2 = 0
for i in dane1:
    i = i[:-1]
    licznik3 = 0
    for ii in range(0, 10):
        if int(i.split(" ")[ii]) % 2 == 0:
            licznik3 += 1
    c.append(licznik3)
for i in dane2:
    i = i[:-1]
    licznik3 = 0
    for ii in range(0, 10):
        if int(i.split(" ")[ii]) % 2 == 0:
            licznik3 += 1
    d.append(licznik3)
for i in range(0, len(c)):
    if c[i] == 5 and d[i] == 5:
        licznik2 += 1
print("Zadanie 4.2")
print(licznik2)


def dane(i):
    i = i[:-1]
    e = []
    for ii in i.split(" "):
        if ii not in e:
            e.append(ii)
    e.sort()
    return e


licznik3 = 0
f = ""
for i in range(0, len(dane1)):
    if dane(dane1[i]) == dane(dane2[i]):
        licznik3 += 1
        f += str(i+1)
        f += ", "
f = f[:-2]
print("Zadanie 4.3")
print(licznik3, "pary ciągów")
print("Numery wierszy:", f)

print("Zadanie 4.4")
for i in range(0, len(dane1)):
    g = ""
    h = []
    for ii in dane1[i].split(" "):
        h.append(int(ii))
    for ii in dane2[i].split(" "):
        h.append(int(ii))
    h.sort()
    for ii in h:
        g += str(ii)
        g += " "
    print(g)
