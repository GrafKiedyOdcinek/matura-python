plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

maks = 0
print("Zadanie 5.2")
for i in dane:
    i = i[:-1]
    if int(i) > maks and int(i) % 2 == 0:
        maks = int(i)
    if i == i[::-1]:
        print(i)
print("Zadanie 5.1")
print(maks)

print("Zadanie 5.3")
suma1 = 0
for i in dane:
    suma = 0
    i = i.strip()
    for ii in range(0, len(i)):
        suma += int(i[ii])
        suma1 += int(i[ii])
    if suma > 30:
        print(i)
print(suma1)
