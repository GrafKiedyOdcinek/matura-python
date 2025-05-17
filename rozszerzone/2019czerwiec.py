plik1 = open("liczby.txt")
dane1 = plik1.readlines()
plik1.close()
plik2 = open("pierwsze.txt")
dane2 = plik2.readlines()
plik2.close()


def isprimep(l):
    if 100 < l < 5000:
        for i in range(2, l):
            if l % i == 0:
                return False
        else:
            return True
    else:
        return False


print("Zadanie 4.1")
for i in dane1:
    i = i[:-1]
    if isprimep(int(i)) == True:
        print(i)


def isprime(l):
    for i in range(2, l):
        if l % i == 0:
            return False
    else:
        return True


print("Zadanie 4.2")
for i in dane2:
    i = i[:-1]
    if isprime(int(i[::-1])) == True:
        print(i)

def waga(l):
    w = 0
    for i in range(0, len(str(l))):
        w += int(str(l)[i])
    if w < 10:
        return w
    else:
        return waga(w)


licznik = 0
for i in dane2:
    i = i[:-1]
    if waga(i) == 1:
        licznik += 1
print("Zadanie 4.3")
print(licznik)
