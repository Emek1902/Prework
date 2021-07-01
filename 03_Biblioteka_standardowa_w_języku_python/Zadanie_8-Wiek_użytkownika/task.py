name = str(input("Podaj swoje imię: "))
year = int(input("Podaj rok swojego urodzenia: "))

import datetime
now = int(datetime.date.today().year)

age = str(now - year)

print("Użytkownik: " + name + " jest w wieku " + age + " lat.")