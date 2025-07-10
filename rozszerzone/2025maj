plik = open("symbole.txt")
dane = plik.readlines()
plik.close()

print("Zadanie 2.1")
for i in dane:
    i = i.strip("\n")
    if i == i[::-1]:
        print(i)

a = 0
b = ""
for i in range(0, len(dane)):
    for ii in range(1, 12):
        if dane[i][ii] == dane[i][ii-1] == dane[i][ii+1] == dane[i+1][ii] == dane[i+1][ii-1] == dane[i+1][ii+1] == dane[i-1][ii] == dane[i-1][ii-1] == dane[i-1][ii+1]:
            a += 1
            b += str(i+1)+" "+str(ii+1)+" "
print("Zadanie 2.2")
c = str(a)+" "
c += b
print(c)


def symbole(l):
    liczba = ""
    for i in l:
        if i == "o":
            liczba += "0"
        if i == "+":
            liczba += "1"
        if i == "*":
            liczba += "2"
    return int(liczba, 3)


a = []
for i in dane:
    i = symbole(i.strip("\n"))
    a.append(i)
b = 0
c = str(max(a))+" "
for i in a:
    if i == max(a):
        c += dane[b].strip("\n")
    b += 1
print("Zadanie 2.3")
print(c)


def trojkowy(l):
    a = ""
    while l != 0:
        a += str(l % 3)
        l = l//3
    return a[::-1]


def symbole2(l):
    symbol = ""
    for i in l:
        if i == "0":
            symbol += "o"
        if i == "1":
            symbol += "+"
        if i == "2":
            symbol += "*"
    return symbol

print("Zadanie 2.4")
print(sum(a), symbole2(trojkowy(sum(a))))

from math import gcd
plik2 = open("dron.txt")
dane2 = plik2.readlines()
plik2.close()

a = 0
for i in dane2:
    i = i.strip("\n")
    if gcd(abs(int(i.split(" ")[0])), abs(int(i.split(" ")[1]))) > 1:
        a += 1
print("Zadanie 3.1")
print(a)

a = []
b = [0, 0]
for i in dane2:
    i = i.strip("\n")
    b[0] += int(i.split(" ")[0])
    b[1] += int(i.split(" ")[1])
    a.append([b[0], b[1]])
c = 0
for i in a:
    if i[0] < 5000 and i[1] < 5000:
        c += 1
print("Zadanie 3.2a")
print(c)

b = []
for i in range(0, len(a)):
    for ii in range(i, len(a)):
        if (a[i][0]+a[ii][0]) % 2 == 0 and (a[i][1]+a[ii][1]) % 2 == 0 and a[i][0] != a[ii][0]:
            b.append([(a[i][0]+a[ii][0])//2, (a[i][1]+a[ii][1])//2])
c = []
for i in b:
    if i in a:
        c = [i[0], i[1]]
print("Zadanie 3.2b")
for i in range(0, len(a)):
    for ii in range(i, len(a)):
        if (a[i][0]+a[ii][0]) % 2 == 0 and (a[i][1]+a[ii][1]) % 2 == 0 and a[i][0] != a[ii][0]:
            if c[0] == (a[i][0]+a[ii][0])//2 and c[1] == (a[i][1]+a[ii][1])//2:
                print("("+str(a[i][0])+", "+str(a[i][1])+"), ("+str(c[0])+", "+str(c[1])+"), ("+str(a[ii][0])+", "+str(a[ii][1])+")")
