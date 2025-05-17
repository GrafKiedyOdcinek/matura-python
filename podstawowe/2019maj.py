plik = open("dane.txt")
dane = plik.readlines()
plik.close()

k = 0
m = 0
licznik = 0
print("Zadanie 6.3")
for i in dane:
    i = i[:-1]
    if int(i[9]) % 2 == 0:
        k += 1
    if int(i[9]) % 2 == 1:
        m += 1
    if int(i[2]+i[3]) == 11 or int(i[2]+i[3]) == 31:
        licznik += 1
    if (int(i[0]) + 3 * int(i[1]) + 7 * int(i[2]) + 9 * int(i[3]) + int(i[4]) + 3 * int(i[5]) + 7 * int(i[6]) + 9 * int(i[7]) + int(i[8]) + 3 * int(i[9]) + int(i[10])) % 10 != 0:
        print(i)
print("Zadanie 6.1")
print(k)
print(m)
print("Zadanie 6.2")
print(licznik)
