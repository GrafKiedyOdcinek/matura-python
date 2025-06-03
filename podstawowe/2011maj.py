plik = open("hasla.txt")
dane = plik.readlines()
plik.close()

a = 0
for i in dane:
    i = i.strip("\n")
    if len(i) % 2 == 0:
        a += 1
print("Zadanie 4a")
print("Parzyste:", a, "Nieparzyste:", 200-a)
print("Zadanie 4b")
for i in dane:
    i = i.strip("\n")
    if i == i[::-1]:
        print(i)
print("Zadanie 4c")
for i in dane:
    b = 0
    i = i.strip("\n")
    for ii in range(0, len(i)-1):
        if ord(i[ii])+ord(i[ii+1]) == 220 and b == 0:
            print(i)
            b += 1
