plik = open("instrukcje.txt")
dane = plik.readlines()
plik.close()


def przesun(l, z):
    g = -1
    if ord(z) != 90:
        x = ord(z)+1
    else:
        x = 65
    for i in range(0, len(l)):
        g += 1
        if l[i] == z:
            a.pop(g)
            a.insert(g, chr(x))
            return a


a = []
for i in dane:
    i = i.strip("\n")
    if i.split(" ")[0] == "DOPISZ":
        a.append(i.split(" ")[1])
    if i == "USUN 1":
        a.pop(-1)
    if i.split(" ")[0] == "ZMIEN":
        a[-1] = i.split(" ")[1]
    if i.split(" ")[0] == "PRZESUN":
        a = przesun(a, i.split(" ")[1])
print("Zadanie 4.1")
print(len(a))

b = []
licznik = 1
maks = 0
c = []
for i in dane:
    i = i.strip("\n").split(" ")[0]
    b.append(i)
for i in range(0, len(b)-1):
    if b[i] == b[i+1]:
        licznik += 1
    else:
        licznik = 1
    if licznik > maks:
        maks = licznik
        c.append(b[i])
print("Zadanie 4.2")
print(c[-1], maks)

d = []
m = 0
e = []
for i in dane:
    i = i.strip("\n")
    if i.split(" ")[0] == "DOPISZ":
        d.append(i.split(" ")[1])
for i in d:
    if d.count(i) > m:
        m = d.count(i)
        e.append(i)
print("Zadanie 4.3")
print(e[-1], m)
p = ""
for i in a:
    p += i
print("Zadanie 4.4")
print(p)
