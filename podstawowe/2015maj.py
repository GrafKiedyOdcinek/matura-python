plik1 = open("slowa.txt")
dane1 = plik1.readlines()
plik1.close()

dlugosc1 = 0
dlugosc2 = 0
dlugosc3 = 0
dlugosc4 = 0
dlugosc5 = 0
dlugosc6 = 0
dlugosc7 = 0
dlugosc8 = 0
dlugosc9 = 0
dlugosc10 = 0
dlugosc11 = 0
dlugosc12 = 0
for i in dane1:
    i = i[:-1]
    if len(i) == 1:
        dlugosc1 += 1
    if len(i) == 2:
        dlugosc2 += 1
    if len(i) == 3:
        dlugosc3 += 1
    if len(i) == 4:
        dlugosc4 += 1
    if len(i) == 5:
        dlugosc5 += 1
    if len(i) == 6:
        dlugosc6 += 1
    if len(i) == 7:
        dlugosc7 += 1
    if len(i) == 8:
        dlugosc8 += 1
    if len(i) == 9:
        dlugosc9 += 1
    if len(i) == 10:
        dlugosc10 += 1
    if len(i) == 11:
        dlugosc11 += 1
    if len(i) == 12:
        dlugosc12 += 1
print("Zadanie 5.1")
print("1", dlugosc1)
print("2", dlugosc2)
print("3", dlugosc3)
print("4", dlugosc4)
print("5", dlugosc5)
print("6", dlugosc6)
print("7", dlugosc7)
print("8", dlugosc8)
print("9", dlugosc9)
print("10", dlugosc10)
print("11", dlugosc11)
print("12", dlugosc12)

plik2 = open("nowe.txt")
dane2 = plik2.readlines()
plik2.close()
slowa = {}
for i in dane2:
    licznik_slow = 0
    licznik_lustrzanych = 0
    i = i[:-1]
    i_lustrzane = i[::-1]
    for ii in dane1:
        ii = ii.strip("\n")
        if i == ii:
            licznik_slow += 1
        if i_lustrzane == ii:
            licznik_lustrzanych += 1
    slowa[i] = (licznik_slow, licznik_lustrzanych)
print("Zadanie 5.2")
print(slowa)
