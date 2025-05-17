plik = open("identyfikator.txt")
dane = plik.readlines()
plik.close()

c = 0
e = []
for i in dane:
    i = i.strip("\n")
    a = []
    b = 0
    for ii in i:
        a.append(ii)
    a.pop(0)
    a.pop(0)
    a.pop(0)
    for ii in a:
        b += int(ii)
    if b > c:
        c = b
for i in dane:
    i = i.strip("\n")
    a = []
    b = 0
    for ii in i:
        a.append(ii)
    a.pop(0)
    a.pop(0)
    a.pop(0)
    for ii in a:
        b += int(ii)
    if b == c:
        e.append(i)
print("Zadanie 4.1")
for i in range(0, len(e)):
    print(e[i])

print("Zadanie 4.2")
for i in dane:
    i = i.strip("\n")
    a = []
    c = []
    for ii in i:
        a.append(ii)
    c.append(a[0])
    a.pop(0)
    c.append(a[0])
    a.pop(0)
    c.append(a[0])
    a.pop(0)
    if c == c[::-1] or a == a[::-1]:
        print(i)

print("Zadanie 4.3")
for i in dane:
    i = i.strip("\n")
    a = []
    b = 0
    c = []
    suma = 0
    for ii in i:
        a.append(ii)
    c.append(a[0])
    a.pop(0)
    c.append(a[0])
    a.pop(0)
    c.append(a[0])
    a.pop(0)
    b = int(a[0])
    a.pop(0)
    suma += (ord(c[0])-55)*7
    suma += (ord(c[1])-55)*3
    suma += ord(c[2])-55
    suma += int(a[0])*7
    suma += int(a[1])*3
    suma += int(a[2])
    suma += int(a[3])*7
    suma += int(a[4])*3
    suma = suma % 10
    if suma != b:
        print(i)
