plik = open("anagram.txt")
dane = plik.readlines()
plik.close()

az = 0
ap = 0
for i in dane:
    i = i.strip("\n")
    a0 = i.count("0")
    a1 = i.count("1")
    if a0 == a1:
        az += 1
    if abs(a0-a1) == 1:
        ap += 1
print("Zadanie 3.1")
print(az)
print(ap)

print("Zadanie 3.2")
for i in dane:
    i = i.strip("\n")
    if len(i) == 8 and 5 > i.count("0") > 2:
        print(i)

a = []
for i in range(0, len(dane)-1):
    a.append(int(bin(abs(int(dane[i].strip("\n"), 2) - int(dane[i+1].strip("\n"), 2)))[2:]))
print("Zadanie 3.3")
print(max(a))

a = 0
d = []
for i in dane:
    b = []
    c = 0
    i = str(int(i.strip("\n"), 2))
    if i.count("0") == 0:
        a += 1
    for ii in i:
        if int(ii) not in b:
            b.append(int(ii))
    for ii in b:
        c += ii
    d.append([c, i])
e = []
for i in d:
    if i[0] == max(d)[0]:
        e.append(i)
print("Zadanie 3.4")
print(a)
print(e[0][1])
