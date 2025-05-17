plik1 = open("dane_6_1.txt")
dane1 = plik1.readlines()
plik1.close()


def szyfrowanie(l, k):
    b = ""
    for ii in l:
        a = ord(ii)+k
        while a > 90:
            a -= 26
        b += chr(a)
    return b


print("Zadanie 6.1")
for i in dane1:
    i = i[:-1]
    print(szyfrowanie(i, 107))


plik2 = open("dane_6_2.txt")
dane2 = plik2.readlines()
plik2.close()


def odszyfrowywanie(l, k):
    b = ""
    for ii in l:
        a = ord(ii)-k
        while a < 65:
            a += 26
        b += chr(a)
    return b


print("Zadanie 6.2")
for i in dane2:
    i = i[:-1]
    a = i.split(" ")[0]
    if i.split(" ")[1] == "":
        b = 0
    else:
        b = int(i.split(" ")[1])
    print(odszyfrowywanie(a, b))


plik3 = open("dane_6_3.txt")
dane3 = plik3.readlines()
plik3.close()


def bledne(l):
    a = []
    b = []
    c = 0
    l = l[:-1]
    for ii in l.split(" ")[0]:
        a.append(ord(ii))
    for ii in l.split(" ")[1]:
        c += 1
        b.append((ord(ii) - a[c-1]) % 26)
    return b


print("Zadanie 6.3")
for i in dane3:
    if bledne(i).count(bledne(i)[0]) != len(bledne(i)):
        print(i.split(" ")[0])
