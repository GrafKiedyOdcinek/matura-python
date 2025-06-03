plik = open("dane.txt")
dane = plik.readlines()
plik.close()

for i in dane:
    i = i.strip("\n")
    if i == i[::-1]:
        print(i)
