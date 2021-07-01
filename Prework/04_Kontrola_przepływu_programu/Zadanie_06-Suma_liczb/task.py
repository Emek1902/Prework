liczba = input("Podaj liczbę naturalną: ")

naturalna = int(abs(round(float(liczba), 0)))

lista = []

for i in range(0, naturalna + 1, 1):
    lista.append(i)

suma = sum(lista)
print(suma)