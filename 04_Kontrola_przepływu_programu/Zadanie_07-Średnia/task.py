numbers = []

n = int(input("Podaj, ile liczb chcesz wprowadzić: "))

for i in range(1, n+1, 1):
    liczba = int(input("Podaj liczbę: "))
    numbers.append(liczba)

suma = sum(numbers)
srednia = round(suma / n, 2)

separator = ""
wyswietlone = separator.join(str(numbers))
print("Wprowadzone liczby (łącznie " + str(n) + "): " + wyswietlone)

print("Suma liczb: " + str(suma))
print("Średnia liczb: " + str(srednia))

if suma > srednia:
    print("Suma jest większa od średniej")
elif suma < srednia:
    print("Srednia jest większa od sumy")
else:
    print("Suma i średnia są równe")