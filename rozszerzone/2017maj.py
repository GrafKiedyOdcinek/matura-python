plik = open("dane.txt")
dane = plik.readlines()
plik.close()

max = 0
min = float('inf')

for i in dane:
    i = i[:-1]
    a = i.split(" ")
    for ii in a:
        if int(ii) > max:
            max = int(ii)
        if int(ii) < min:
            min = int(ii)
print("Zadanie 6.1")
print(max, min)

licznik = 0
for i in dane:
    i = i[:-1]
    a = i.split(" ")
    if a != a[::-1]:
        licznik += 1
print("Zadanie 6.2")
print(licznik)

dane2 = []
for i in dane:
    i = i.strip().split()
    a = []
    for ii in i:
        a.append(int(ii))
    dane2.append(a)
licznik2 = 0
for i in range(len(dane2)):
    for ii in range(len(dane2[i])):
        if ii != 0 and (dane2[i][ii] - dane2[i][ii-1] > 128 or dane2[i][ii] - dane2[i][ii-1] < -128):
            licznik2 += 1
        elif (ii + 1) < len(dane2[i]) and (dane2[i][ii+1] - dane2[i][ii] > 128 or dane2[i][ii+1] - dane2[i][ii] < -128):
            licznik2 += 1
        elif i != 0 and (dane2[i][ii] - dane2[i-1][ii] > 128 or dane2[i][ii] - dane2[i-1][ii] < -128):
            licznik2 += 1
        elif (i+1) < len(dane2) and (dane2[i+1][ii] - dane2[i][ii] > 128 or dane2[i+1][ii] - dane2[i][ii] < -128):
            licznik2 += 1
print("Zadanie 6.3")
print(licznik2)

licznik3 = 0
maks = 0
for i in range(len(dane2)):
    for ii in range(1, len(dane2)):
        if dane2[ii][i] == dane2[ii-1][i]:
            licznik3 += 1
        else:
            if licznik3 > maks:
                maks = licznik3
            licznik3 = 1
print("Zadanie 6.4")
print(maks)
