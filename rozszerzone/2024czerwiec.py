plik = open("slowa.txt")
dane = plik.readlines()
plik.close()

a = 0
for i in dane:
    i = i.strip("\n")
    for ii in range(0, len(i)-2):
        if i[ii] == "k" and i[ii+2] == "t":
            a += 1
print("Zadanie 3.1")
print(a)


def szyfrowanie(l):
    b = ""
    for ii in l:
        a = ord(ii)+13
        while a > 122:
            a -= 26
        b += chr(a)
    return b


b = 0
c = []
for i in dane:
    i = i.strip("\n")
    if i[::-1] == szyfrowanie(i):
        b += 1
        c.append([len(i), i])
print("Zadanie 3.2")
print(b)
print(max(c)[1])

a = []
for i in dane:
    i = i.strip("\n")
    for ii in i:
        if i.count(ii) > len(i)/2:
            a.append(i)
b = []
for i in a:
    if i not in b:
        b.append(i)
print("Zadanie 3.3")
for i in b:
    print(i)
