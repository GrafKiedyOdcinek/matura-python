def kodowanie(n):
    if n == 0:
        return "10101110111010"
    if n == 1:
        return "11101010101110"
    if n == 2:
        return "10111010101110"
    if n == 3:
        return "11101110101010"
    if n == 4:
        return "10101110101110"
    if n == 5:
        return "11101011101010"
    if n == 6:
        return "10111011101010"
    if n == 7:
        return "10101011101110"
    if n == 8:
        return "11101010111010"
    if n == 9:
        return "10111010111010"


plik = open("kody.txt")
dane = plik.readlines()
plik.close()

print("Zadanie 6.1")
for i in dane:
    i = i.strip()
    print(int(i[1]) + int(i[3]) + int(i[5]), int(i[0]) + int(i[2]) + int(i[4]))

print("Zadanie 6.2")
for i in dane:
    i = i.strip()
    print((10 - ((int(i[1]) + int(i[3]) + int(i[5]) + int(i[0]) + int(i[2]) + int(i[4])) % 10)) % 10, i)

print("Zadanie 6.3")
for i in dane:
    i = i[:-1]
    print("11011010" + kodowanie(int(i[0])) + kodowanie(int(i[1])) + kodowanie(int(i[2])) + kodowanie(int(i[3])) + kodowanie(int(i[4])) + kodowanie(int(i[5])) + kodowanie(int((10 - ((int(i[1]) + int(i[3]) + int(i[5]) + int(i[0]) + int(i[2]) + int(i[4])) % 10)) % 10)) + "11010110")
