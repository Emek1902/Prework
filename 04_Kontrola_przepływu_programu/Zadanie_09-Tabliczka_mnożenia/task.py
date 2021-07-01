n = int(input("Podaj liczbę: "))

if n < 1 or n > 10:
    print("Podano liczbę spoza zakresu 1 do 10")
    exit()

for i in range(1, 11, 1):
    iloczyn = i * n
    print(str(i) + " * " + str(n) + " = " + str(iloczyn))
    i += 1