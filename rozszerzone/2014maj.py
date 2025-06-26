plik = open("NAPIS.txt")
dane = plik.readlines()
plik.close()


def isprime(l):
    if l < 2:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    else:
        return True

b = 0
for i in dane:
    i = i.strip("\n")
    a = 0
    for ii in i:
        a += ord(ii)
    if isprime(a) == True:
        b += 1
print("Zadanie 5a")
print(b)


def rosnacy(n):
    a = True
    for i in range(0, len(n)-1):
        if ord(n[i]) >= ord(n[i+1]):
            a = False
    return a


print("Zadanie 5b")
for i in dane:
    i = i.strip("\n")
    if rosnacy(i) == True:
        print(i)

a = []
b = []
c = []
for i in dane:
    i = i.strip("\n")
    a.append(i)
for i in range(0, len(dane)):
    if a.count(a[i]) > 1:
        b.append(a[i])
for i in b:
    if i not in c:
        c.append(i)
print("Zadanie 5c")
for i in c:
    print(i)
