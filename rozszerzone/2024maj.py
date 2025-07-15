plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

a = []
b = []
for i in dane[0].strip("\n").split(" "):
    a.append(int(i))
for i in dane[1].strip("\n").split(" "):
    b.append(int(i))
d = 0
for i in range(0, len(a)):
    c = 0
    for ii in b:
        if ii % a[i] == 0:
            c += 1
    if c > 0:
        d += 1
print("Zadanie 4.1")
print(d)
print("Zadanie 4.2")
a_s = sorted(a)[::-1]
print(a_s[100])
print("Zadanie 4.3")
for i in b:
    f = i
    for ii in a:
        if f % ii == 0:
            f = f // ii
    if f == 1:
        print(i)
n = 0
for i in range(0, len(a)):
    s = sum(a[i:i+50])
    do = 50
    so = s / do
    if so > n:
        n = so
        p = i
        d = do
    for ii in range(i+50, len(a)):
        s += a[ii]
        do += 1
        so = s / do
        if so > n:
            n = so
            p = i
            d = do
print("Zadanie 4.4")
print(n, d, a[p])
