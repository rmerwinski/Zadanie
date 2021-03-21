import math

def dodawanie():
    print("DODAWANIE:")
    a = input("podaj składnik 1:")
    b = input("podaj składnik 2:")
    try:
        s = float(a) + float(b)
        print("Wynik=", s)
    except ValueError:
        print("Błędne dane")

def odejmowanie():
    a = input("podaj odjemną:")
    b = input("podaj odjemnik:")
    try:
        r = float(a) - float(b)
        print("Wynik=", r)
    except ValueError:
        print("Błędne dane")

def mnożenie():
    a = input("podaj czynnik 1:")
    b = input("podaj czynnik 2:")
    try:
        w = float(a) * float(b)
        print("Wynik=", w)
    except ValueError:
        print("Błędne dane")

def dzielenie():
    a = input("podaj dzielną:")
    b = input("podaj dzielnik:")
    try:
        w = float(a) / float(b)
        print("Wynik=", w)
    except ValueError:
        print("Błędne dane")
    except ZeroDivisionError:
        print("Nie możesz dzielić przez 0!")

def potegowanie():
    a = input("podaj podstawę:")
    b = input("podaj wykładnik:")
    try:
        w = float(a) ** float(b)
        print("Wynik=", w)
    except ValueError:
        print("Błędne dane")
    except OverflowError:
        print("Wynik zbyt duży, spróbuj mniejsze liczby")
        potegowanie()

def pierwiastkowanie():
    a = input("podaj liczbę pierwiastkowaną:")
    try:
        w = math.sqrt(float(a))
        print("Wynik=", w)
    except ValueError:
        print("Błędne dane")

def sin():
    a = input("podaj kąt :")
    try:
        w = math.sin(float(a))
        print("Wynik=", w)
    except ValueError:
        print("Błędne dane")

def cos():
    a = input("podaj kąt :")
    try:
        w = math.cos(float(a))
        print("Wynik=", w)
    except ValueError:
        print("Błędne dane")

def tan():
    a = input("podaj kąt :")
    try:
        w = math.tan(float(a))
        print("Wynik=", w)
    except ValueError:
        print("Błędne dane")

def menu():
    print("MENU:")
    print("1. DODAWANIE")
    print("2. ODEJMOWANIE")
    print("3. MNOŻENIE")
    print("4. DZIELENIE")
    print("5. POTĘGOWANIE")
    print("6. PIERWIASTEK KWADRATOWY")
    print("7. SINUS")
    print("8. COSINUS")
    print("9. TANGENS")
    print("0. WYJŚCIE")

def funkcja():
    operacja = input("Co wybierzesz ? ")
    if operacja == "1":
        dodawanie()
    elif operacja == "2":
        odejmowanie()
    elif operacja == "3":
        mnożenie()
    elif operacja == "4":
        dzielenie()
    elif operacja == "5":
        potegowanie()
    elif operacja == "6":
        pierwiastkowanie()
    elif operacja == "7":
        sin()
    elif operacja == "8":
        cos()
    elif operacja == "9":
        tan()
    elif operacja == "0":
       exit()
    else:
        print("Błąd")
        menu()
        funkcja()
    menu()
    funkcja()

menu()
funkcja()

