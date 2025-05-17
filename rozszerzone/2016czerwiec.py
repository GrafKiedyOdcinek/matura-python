plik = open("liczby.txt")
dane = plik.readlines()
plik.close()

licznik1 = 0
licznik2 = 0
licznik3 = 0
for i in dane:
    i = i[:-1]
    if i[-1] == "8":
        licznik1 += 1
    if i[-1] == "4" and i.count("0") == 0:
        licznik2 += 1
    if i[-1] == "2":
        i = int(i[:-1], 2)
        if i % 2 == 0:
            licznik3 += 1
print("Zadanie 6.1")
print(licznik1)
print("Zadanie 6.2")
print(licznik2)
print("Zadanie 6.3")
print(licznik3)

licznik4 = 0
for i in dane:
    i = i[:-1]
    if i[-1] == "8":
        i = int(i[:-1], 8)
        licznik4 += i
print("Zadanie 6.4")
print(licznik4)

min = float('inf')
max = 0
a = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
for i in dane:
    i = i[:-1]
    if i[-1] == "2":
        a2.append(int(i[:-1], 2))
        a.append(int(i[:-1], 2))
for i in dane:
    i = i[:-1]
    if i[-1] == "3":
        a3.append(int(i[:-1], 3))
        a.append(int(i[:-1], 3))
for i in dane:
    i = i[:-1]
    if i[-1] == "4":
        a4.append(int(i[:-1], 4))
        a.append(int(i[:-1], 4))
for i in dane:
    i = i[:-1]
    if i[-1] == "5":
        a5.append(int(i[:-1], 5))
        a.append(int(i[:-1], 5))
for i in dane:
    i = i[:-1]
    if i[-1] == "6":
        a6.append(int(i[:-1], 6))
        a.append(int(i[:-1], 6))
for i in dane:
    i = i[:-1]
    if i[-1] == "7":
        a7.append(int(i[:-1], 7))
        a.append(int(i[:-1], 7))
for i in dane:
    i = i[:-1]
    if i[-1] == "8":
        a8.append(int(i[:-1], 8))
        a.append(int(i[:-1], 8))
for i in dane:
    i = i[:-1]
    if i[-1] == "9":
        a9.append(int(i[:-1], 9))
        a.append(int(i[:-1], 9))
for i in a:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)

print("Zadanie 6.5")
if a2.count(min) >= 1:
    min2 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "2":
            if int(i) < min2:
                min2 = int(i)
    print("najmniejsza:", min, min2)
if a3.count(min) >= 1:
    min3 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "3":
            if int(i) < min3:
                min3 = int(i)
    print("najmniejsza:", min, min3)
if a4.count(min) >= 1:
    min4 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "4":
            if int(i) < min4:
                min4 = int(i)
    print("najmniejsza:", min, min4)
if a5.count(min) >= 1:
    min5 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "5":
            if int(i) < min5:
                min5 = int(i)
    print("najmniejsza:", min, min5)
if a6.count(min) >= 1:
    min6 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "6":
            if int(i) < min6:
                min6 = int(i)
    print("najmniejsza:", min, min6)
if a7.count(min) >= 1:
    min7 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "7":
            if int(i) < min7:
                min7 = int(i)
    print("najmniejsza:", min, min7)
if a8.count(min) >= 1:
    min8 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "8":
            if int(i) < min8:
                min8 = int(i)
    print("najmniejsza:", min, min8)
if a9.count(min) >= 1:
    min9 = float('inf')
    for i in dane:
        i = i[:-1]
        if i[-1] == "9":
            if int(i) < min9:
                min9 = int(i)
    print("najmniejsza:", min, min9)
if a2.count(max) >= 1:
    max2 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "2":
            if int(i) > max2:
                max2 = int(i)
    print("największa:", max, max2)
if a3.count(max) >= 1:
    max3 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "3":
            if int(i) > max3:
                max3 = int(i)
    print("największa:", max, max3)
if a4.count(max) >= 1:
    max4 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "4":
            if int(i) > max4:
                max4 = int(i)
    print("największa:", max, max4)
if a5.count(max) >= 1:
    max5 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "5":
            if int(i) > max5:
                max5 = int(i)
    print("największa:", max, max5)
if a6.count(max) >= 1:
    max6 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "6":
            if int(i) > max6:
                max6 = int(i)
    print("największa:", max, max6)
if a7.count(max) >= 1:
    max7 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "7":
            if int(i) > max7:
                max7 = int(i)
    print("największa:", max, max7)
if a8.count(max) >= 1:
    max8 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "8":
            if int(i) > max8:
                max8 = int(i)
    print("największa:", max, max8)
if a9.count(max) >= 1:
    max9 = 0
    for i in dane:
        i = i[:-1]
        if i[-1] == "9":
            if int(i) > max9:
                max9 = int(i)
    print("największa:", max, max9)
