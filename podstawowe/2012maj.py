plik = open("cyfry.txt")
dane = plik.readlines()
plik.close()

podzielne = 0
for d in dane:
    d = int(d.strip())
    if d % 2 == 0:
        podzielne += 1
print("Zadanie 4a")
print(podzielne)

max_suma = -1
min_suma = 9999999
max_liczba = 0
min_liczba = 0

for d in dane:
    d = d.strip()
    suma = 0
    for i in d:
        suma += int(i)
        if suma > max_suma:
            max_suma = suma
            max_liczba = d
for d in dane:
    d = d.strip()
    suma = 0
    for i in d:
        suma += int(i)
    if suma < min_suma:
        min_suma = suma
        min_liczba = d
print("Zadanie 4b")
print(max_liczba, min_liczba)

rosnoce = []
for d in dane:
    d = d.strip()
    cyfry = []
    for i in d:
        cyfry.append(int(i))
    isRosnoce = True
    for ii in range(len(cyfry)-1):
        if cyfry[ii] >= cyfry[ii+1]:
            isRosnoce = False
            break
    if isRosnoce == True:
        rosnoce.append(d)
print(rosnoce)
