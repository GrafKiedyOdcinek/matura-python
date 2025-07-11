plik = open("dane.txt")
dane = plik.readlines()
plik.close()

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
b = ""
c = []
for i in range(0, len(dane[0])-1):
    if dane[0][i] in a and dane[0][i+1] in a:
        b += dane[0][i]
    elif dane[0][i] in a:
        b += dane[0][i]
    elif len(b) != 0:
        c.append(b)
        b = ""
a = 0
for i in c:
    if i[:2] == "50":
        a += 1
print("Zadanie 3.1")
print(a)
def liczby(s):
    a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in s:
        if i == "0":
            a0 += 1
        if i == "1":
            a1 += 1
        if i == "2":
            a2 += 1
        if i == "3":
            a3 += 1
        if i == "4":
            a4 += 1
        if i == "5":
            a5 += 1
        if i == "6":
            a6 += 1
        if i == "7":
            a7 += 1
        if i == "8":
            a8 += 1
        if i == "9":
            a9 += 1
    b = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
    return b
d = ""
for i in range(0, len(liczby(dane[0]))):
    if liczby(dane[0])[i] == max(liczby(dane[0])):
        d += str(i)
d += " "+str(max(liczby(dane[0])))
print("Zadanie 3.2")
print(d)

print("Zadanie 3.3")
for i in c:
    if i[:1] == "5" and len(i) == 9:
        print(i)

a = []
for i in c:
    if len(i) == 9:
        a.append(i)
e = []
for i in a:
    c = 0
    for ii in liczby(i):
        if ii != 0:
            c += 1
    e.append([c, i])
f = []
for i in e:
    if i[0] == min(e)[0]:
        f.append(i[1])
print("Zadanie 3.4")
for i in f[::-1]:
    print(i)
