plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

b = []
l = 0
for i in dane:
    a = []
    i = i.strip("\n")
    for ii in i:
        a.append(ii)
    if a[0] == a[-1]:
        l += 1
        b.append(i)
print("Zadanie 4.1")
print(l, b[0])


def isprime(l):
    if l < 2:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


def dzielniki(k):
    d = []
    e = []
    if isprime(k) == True:
        d.append(k)
    for i in range(2, k):
        if k % i == 0:
            k = k//i
            d.append(i)
            if isprime(k) == True and k > 1:
                d.append(k)
                k = 1
    for i in d:
        if isprime(i):
            e.append(i)
        else:
            for ii in dzielniki(i):
                e.append(ii)
    return e


maks1 = 0
maks2 = 0
a = []
b = []
for i in dane:
    c = []
    i = int(i.strip("\n"))
    if len(dzielniki(i)) > maks1:
        maks1 = len(dzielniki(i))
        a.append(i)
    for ii in dzielniki(i):
        if ii not in c:
            c.append(ii)
    if len(c) > maks2:
        maks2 = len(c)
        b.append(i)
print("Zadanie 4.2")
print(a[-1], maks1, b[-1], maks2)

print("Zadanie 4.3")
l = 0
l2 = 0
e = []
f = []
for i in dane:
    i = int(i.strip("\n"))
    a = []
    b = []
    c = []
    d = []
    a.append(i)
    for i in dane:
        i = int(i.strip("\n"))
        if i % a[0] == 0 and i != a[0]:
            b.append(i)
        for ii in range(0, len(b)):
            if len(b) > 0 and i % b[ii] == 0:
                c.append(b[ii])
    if len(b) > 0 and len(c) > 0:
        for ii in c:
            if ii not in d:
                d.append(ii)
        for ii in range(0, len(d)):
            for iii in range(0, len(b)):
                if d[ii] % b[iii] == 0 and b[iii] < d[ii]:
                    l += 1
                    print(a[0], b[iii], d[ii])
                    e.append(d[ii])
for i in e:
    if i not in f:
        f.append(i)
for i in f:
    g = []
    h = []
    j = []
    for ii in f:
        if ii % i == 0 and ii > i:
            g.append(ii)
    if len(g) > 1:
        for iii in range(0, len(g)):
            for iv in range(0, len(g)):
                if g[iv] % g[iii] == 0 and g[iv] > g[iii]:
                    h.append(g[iv])
        for ii in h:
            if ii not in j:
                j.append(ii)
        l2 += 1
print("a)", l)
print("b)", l2)
