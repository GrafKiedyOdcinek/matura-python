plik = open("napisy.txt")
dane = plik.readlines()
plik.close()

licznik = 0
for i in dane:
    i = i.strip("\n")
    for ii in i:
        if ii.isdigit() == True:
            licznik += 1
print("Zadanie 4.1")
print(licznik)

l = -1
a = ""
for i in dane[19::20]:
    l += 1
    i = i.strip("\n")
    a += i[l]
print("Zadanie 4.2")
print(a)

c = []
d = []
e = ""
g = ""
h = 0
j = ""
for i in dane:
    b = []
    i = i.strip("\n")
    for ii in i:
        if ii.isdigit() == True:
            b.append(ii)
    if len(b) % 2 == 1:
        b.pop(-1)
        for ii in b:
            c.append(ii)
    else:
        for ii in b:
            c.append(ii)
for i in c:
    e += i
    if len(e) == 2:
        d.append(int(e))
        e = ""
for i in d:
    if 65 <= i <= 90:
        g += chr(i)
for i in g:
    if i == "X":
        h += 1
    if h < 3:
        j += i
j += "X"
print("Zadanie 4.4")
print(j)

k = ""
for i in dane:
    a1 = []
    a2 = []
    i = i.strip("\n")
    a1.append(i[-1]+i)
    a2.append(i+i[0])
    if a1[0] == a1[0][::-1] or a2[0] == a2[0][::-1]:
        if a1[0] == a1[0][::-1]:
            for ii in range(0, len(a1[0])):
                if ii == 25:
                    k += a1[0][ii]
        if a2[0] == a2[0][::-1]:
            for ii in range(0, len(a2[0])):
                if ii == 25:
                    k += a2[0][ii]
print("Zadanie 4.3")
print(k)
