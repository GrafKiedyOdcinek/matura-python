plik = open("dane.txt")
dane = plik.readlines()
plik.close()

a = 0
for i in dane:
    i = i.strip("\n")
    if i[0] == i[-1]:
        a += 1
print("Zadanie 6a")
print(a)

a = 0
for i in dane:
    i = str(int(i.strip("\n"), 8))
    if i[0] == i[-1]:
        a += 1
print("Zadanie 6b")
print(a)

def rosnacy(n):
    a = True
    for i in range(0, len(n)-1):
        if int(n[i]) > int(n[i+1]):
            a = False
    return a


a = 0
b = []
for i in dane:
    i = i.strip("\n")
    if rosnacy(i) == True:
        a += 1
        b.append(int(i))
print(a)
print(min(b))
print(max(b))
