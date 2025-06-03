plik = open("liczby.txt")
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


a = []
for i in range(0, 1087):
    if isprime(i) == True:
        a.append(i**2)
for i in dane:
    i = int(i.strip("\n"))
    if i in a:
        print(i)
