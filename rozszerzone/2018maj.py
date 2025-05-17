plik = open("sygnaly.txt")
dane = plik.readlines()
plik.close()

haslo = ""
l = 0
for i in dane:
    l += 1
    i = i[:-1]
    if l % 40 == 0:
        haslo += i[9]
print("Zadanie 4.1")
print(haslo)

maks = 0
c = []
for i in dane:
    i = i[:-1]
    a = []
    for ii in i:
        a.append(ii)
    b = []
    for ii in a:
        if ii not in b:
            b.append(ii)
    if len(b) > maks:
        maks = len(b)
        c.append(i)
print("Zadanie 4.2")
print(c[-1])
print(maks)


def odleglosc(a, b):
    if ord(a) - ord(b) > 10 or ord(a) - ord(b) < -10:
        return False
    else:
        return True


def slowo(s):
    global a
    for i in s:
        a.append(i)
        a.sort()
    if odleglosc(a[0], a[-1]) == False:
        return False
    else:
        return True


print("Zadanie 4.3")
for i in dane:
    i = i[:-1]
    a = []
    if slowo(i) == True:
        print(i)
