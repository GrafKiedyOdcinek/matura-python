plik = open("anagram.txt")
dane = plik.readlines()
plik.close()

print("Zadanie 4a")
for i in dane:
    if len(i.split(" ")[0]) == len(i.split(" ")[1]) == len(i.split(" ")[2]) == len(i.split(" ")[3]) == len(i.split(" ")[4].strip("\n")):
        print(i.strip("\n"))

print("Zadanie 4b")
for i in dane:
    a, b, c, d, e = i.split(" ")[0], i.split(" ")[1], i.split(" ")[2], i.split(" ")[3], i.split(" ")[4].strip("\n")
    f, g, h, j, k = [], [], [], [], []
    for ii in a:
        f.append(ii)
    for ii in b:
        g.append(ii)
    for ii in c:
        h.append(ii)
    for ii in d:
        j.append(ii)
    for ii in e:
        k.append(ii)
    if sorted(f) == sorted(g) == sorted(h) == sorted(j) == sorted(k):
        print(i.strip("\n"))
