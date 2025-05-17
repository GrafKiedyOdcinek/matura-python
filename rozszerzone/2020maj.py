plik = open("pary.txt")
dane = plik.readlines()
plik.close()


def isprime(l):
    for i in range(2, l):
        if l % i == 0:
            return False
    else:
        return True


a = []
for i in range(2, 100):
    if isprime(i) == True and i % 2 == 1:
        a.append(i)

def goldbach(l):
    if l < 4:
        return False
    else:
        for i in a:
            for ii in a:
                if i + ii == l:
                    return l, i, ii
        else:
            return False


print("Zadanie 4.1")
for i in dane:
    i = i[:-1]
    if goldbach(int(i.split(" ")[0])) != False:
        print(goldbach(int(i.split(" ")[0]))[0], goldbach(int(i.split(" ")[0]))[1], goldbach(int(i.split(" ")[0]))[2])

print("Zadanie 4.2")
for i in dane:
    a = []
    i = i[:-1]
    licznik = 1
    maks = 0
    b = ""
    c = ""
    for ii in i.split(" ")[1]:
        a.append(ii)
    for ii in range(0, len(a)-1):
        if i.split(" ")[1][ii] != i.split(" ")[1][ii + 1]:
            licznik = 1
        if i.split(" ")[1][ii] == i.split(" ")[1][ii+1]:
            licznik += 1
        if licznik > maks:
            maks = licznik
            b += i.split(" ")[1][ii]
    for ii in range(0, maks):
        c += b[-1]
    print(c, maks)

d = []
e = []
f = []
for i in dane:
    i = i[:-1]
    if int(i.split(" ")[0]) == len(i.split(" ")[1]):
        d.append(i)
        e.append(int(i.split(" ")[0]))
for i in range(0, len(d)):
    if int(d[i].split(" ")[0]) == min(e):
        f.append(d[i])
print("Zadanie 4.3")
print(min(f))
