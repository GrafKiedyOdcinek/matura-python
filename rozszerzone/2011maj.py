plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

a = 0
for i in dane:
    i = int(i.strip("\n"), 2)
    if i % 2 == 0:
        a += 1
print("Zadanie 6a")
print(a)

a = []
for i in dane:
    i = int(i.strip("\n"), 2)
    a.append(i)
print("Zadanie 6b")
print(str(bin(max(a))[2:]))
print(max(a))

a = 0
b = 0
for i in dane:
    i = i.strip("\n")
    if len(str(i)) == 9:
        b += 1
        a += int(i, 2)
print("Zadanie 6c")
print(b)
print(str(bin(a))[2:])
