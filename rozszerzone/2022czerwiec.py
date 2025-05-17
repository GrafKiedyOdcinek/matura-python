plik = open("liczby.txt")
dane = plik.readlines()
plik.close()


def isprime(l):
    if l < 2:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


e = []
f = ""
print("Zadanie 4.1")
for i in dane:
    a = []
    b = ""
    d = ""
    maks = 0
    i = i.strip("\n")
    for ii in i:
        a.append(ii)
        d += ii
    c = a[::-1]
    for ii in range(0, len(a)):
        b += c[ii]
    if int(b) % 17 == 0:
        print(b)
    e.append(abs(int(d)-int(b)))

for ii in range(0, len(e)):
    if max(e) == e[ii]:
        f += str(dane[ii].strip("\n"))
f += " "
f += str(max(e))
print("Zadanie 4.2")
print(f)

print("Zadanie 4.3")
for i in dane:
    a = []
    b = ""
    d = ""
    i = i.strip("\n")
    for ii in i:
        a.append(ii)
        d += ii
    c = a[::-1]
    for ii in range(0, len(a)):
        b += c[ii]
    if isprime(int(b)) == True and isprime(int(d)) == True:
        print(d)

a = []
k = ""
for i in dane:
    i = i.strip("\n")
    if i not in a:
        a.append(i)
k += str(len(a))+" "
a = dane
b = []
for i in a:
    if a.count(i) == 2:
        b.append(i)
        a.remove(i)
k += str(len(b))+" "
a = dane
b = []
for i in a:
    if a.count(i) == 3:
        b.append(i)
        a.remove(i)
k += str(len(b))+" "
print("Zadanie 4.4")
print(k)
