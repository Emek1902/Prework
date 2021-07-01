print("Równanie w postaci a*x**2 + b*x + c == 0")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x_1 = round((-b - delta**0.5)/(2*a), 3)
    x_2 = round((-b + delta**0.5)/(2*a), 3)
    print("Pierwiastki równania kwadratowego (delta>0) :\nx_1: " + str(x_1) + "\nx_2: " + str(x_2))
elif delta == 0:
    x_0 = round((-b)/(2*a), 3)
    print("Pierwiastek równania kwadratowego (delta=0) :\nx_0: " + str(x_0))
else:
    print("Brak rozwiązań (delta<0).")