plik = open("pi.txt")
dane = plik.readlines()
plik.close()

a = 0
for i in range(0, len(dane)-1):
    if int(str(dane[i].strip("\n") + dane[i+1].strip("\n"))) > 90:
        a += 1
print("Zadanie 3.1")
print(a)

b = []
c = []
e = 0
g = dane
h = []
for i in range(0, len(dane)-1):
    b.append(int(str(dane[i].strip("\n") + dane[i+1].strip("\n"))))
g = b
for i in range(0, len(b)):
    if g.count(b[i]) > e:
        e = g.count(b[i])
        c.append(str(b[i])+" "+str(g.count(b[i])))
for i in c:
    if i.split(" ")[1] == c[-1].split(" ")[1]:
        h.append(i.split(" ")[0])
l = []
for i in range(0, 10):
    for ii in range(0, 10):
        l.append(str(i)+str(ii))
p = float('inf')
z = []
for i in range(0, len(l)):
    if b.count(int(i)) < p:
        p = b.count(int(i))
        z.append(str(l[i]) + " " + str(b.count(int(i))))
x = []
for i in z:
    if i.split(" ")[1] == z[-1].split(" ")[1]:
        x.append(i.split(" ")[0])
print("Zadanie 3.2")
print(str(min(x)+" "+str(z[-1].split(" ")[1])))
print(str(min(h)+" "+str(c[-1].split(" ")[1])))

v = []
q = []
w = []
for i in range(0, len(dane)-5):
    v.append(str(dane[i].strip("\n")+str(dane[i+1].strip("\n"))+str(dane[i+2].strip("\n"))+str(dane[i+3].strip("\n"))+str(dane[i+4].strip("\n"))+str(dane[i+5].strip("\n"))))
for i in range(0, len(v)):
    if v[i][0] < v[i][1]:
        if v[i][1] >= v[i][2] > v[i][3] > v[i][4] > v[i][5]:
            q.append(v[i])
        if v[i][1] < v[i][2] >= v[i][3] > v[i][4] > v[i][5]:
            q.append(v[i])
        if v[i][1] < v[i][2] < v[i][3] >= v[i][4] > v[i][5]:
            q.append(v[i])
        if v[i][1] < v[i][2] < v[i][3] < v[i][4] > v[i][5]:
            q.append(v[i])
for i in range(0, len(q)):
    if q[i] not in w:
        w.append(q[i])
print("Zadanie 3.3")
print(len(w))

m = []
k = 0
m2 = 0
m3 = []
for i in range(0, len(dane)-5):
    k += 1
    j = i
    ciag = ""
    while dane[i].strip("\n") < dane[i+1].strip("\n"):
        ciag += dane[i].strip("\n")
        i += 1
    while dane[i].strip("\n") == dane[i+1].strip("\n") and dane[i].strip("\n") != dane[i+2].strip("\n"):
        ciag += dane[i].strip("\n")
        i += 1
    while dane[i].strip("\n") > dane[i+1].strip("\n"):
        ciag += dane[i].strip("\n")
        i += 1
    ciag += dane[i].strip("\n")
    m.append(ciag+" "+str(k))
for i in range(0, len(m)):
    if len(m[i].split(" ")[0]) > m2:
        m3.append(m[i])
        m2 = len(m[i].split(" ")[0])
print("Zadanie 3.4")
print(m3[-1])
