plik = open("PARY_LICZB.TXT")
dane = plik.readlines()
plik.close()

licznik_a = 0
for i in dane:
    pary = i.strip().split()
    if int(pary[0]) % int(pary[1]) == 0 or int(pary[1]) % int(pary[0]) == 0:
        licznik_a += 1
print("Zadanie 5a")
print(licznik_a)


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


licznik_b = 0
for i in dane:
    pary = i.strip().split()
    if nwd(int(pary[0]), int(pary[1])) == 1:
        licznik_b += 1
print("Zadanie 5b")
print(licznik_b)

licznik_c = 0
for i in dane:
    pary = i.strip().split()
    suma1 = sum(int(cyfra) for cyfra in pary[0])
    suma2 = sum(int(cyfra) for cyfra in pary[1])
    if suma1 == suma2:
        licznik_c += 1
print("Zadanie 5c")
print(licznik_c)
