# -*- coding: utf-8 -*-
"""Alg_Num2_ZR_AŚ.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MJkj7IukA_zyMqvMK8lLgrofdDjQjOJR

Metoda iteracji prostych
"""

def iteracja_prosta(f, x_0, epsilon, max_iter=1000):
    """
    Funkcja wykonująca iterację prostą dla danej funkcji f i punktu początkowego x_0.
    Sprawdza, czy osiągnięto zadaną dokładność epsilon w max_iter iteracjach.
    """
    for i in range(max_iter):
        x_1 = f(x_0)
        print(f"Iteracja {i+1}: x = {x_1}")
        if abs(x_1 - x_0) < epsilon:
            print(f"Osiągnięto dokładność epsilon = {epsilon} w iteracji {i+1}")
            return x_1, i+1
        x_0 = x_1
    print(f"Nie osiągnięto dokładności epsilon = {epsilon} po {max_iter} iteracjach")
    return x_1, max_iter

def funkcja(x):
    """
    Równanie x = (100 - x)^(1/5)
    """
    return (100 - x) ** (1/5)

def pobierz_dane(nazwa, warunek=None):
    """
    Funkcja do pobierania danych od użytkownika z zabezpieczeniem
    przed wprowadzeniem wartości innych niż liczby lub spełniających warunek.
    """
    while True:
        try:
            wartosc = float(input(f"Podaj {nazwa}: ").replace(',', '.'))  # Zamiana ewentualnego przecinka na kropkę
            if warunek is not None and not warunek(wartosc):
                raise ValueError
            return wartosc
        except ValueError:
            print("Wprowadź poprawną wartość liczbową.")
            if warunek is not None:
                print(f"{nazwa.capitalize()} musi spełniać określony warunek.")

while True:
    # Pobranie danych od użytkownika
    x_start = pobierz_dane("punkt początkowy")
    epsilon = pobierz_dane("dokładność (0 < epsilon < 1)", lambda x: 0 < x < 1 and x > 10**(-14))

    # Wywołanie funkcji iteracji prostej bez podawania maksymalnej liczby iteracji
    wynik, iteracja = iteracja_prosta(funkcja, x_start, epsilon)
    print(f"Ostateczny wynik: x = {wynik} osiągnięty w iteracji {iteracja}")

    # Sprawdzenie czy użytkownik chce powtórzyć operację
    decyzja = input("Czy chcesz powtórzyć operację? (Tak/Nie): ")
    if decyzja.lower() == 'tak':
        continue
    elif decyzja.lower() == 'nie':
        break

"""Metoda siecznych"""

def funkcja1(x):
    """
    Funkcja 0 = x^5 + x - 100
    """
    return x**5 + x - 100

def metoda_siecznych(f, x0, x1, epsilon):
    """
    Metoda siecznych do rozwiązania równania f(x) = 0
    z punktami startowymi x0 i x1 oraz dokładnością epsilon.
    """
    iteracja = 0
    while True:
        iteracja += 1
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        print(f"Iteracja {iteracja}: x_{iteracja +1} = {x2}")

        if abs(x2 - x1) < epsilon:
            print(f"Osiągnięto dokładność epsilon = {epsilon} w iteracji {iteracja}")
            return x2, iteracja

        x0 = x1
        x1 = x2

def pobierz_liczbe(nazwa, warunek=None):
    """
    Funkcja do pobierania liczby od użytkownika z zabezpieczeniem
    przed wprowadzeniem wartości innych niż liczba lub spełniających warunek.
    """
    while True:
        try:
            liczba = float(input(f"Podaj {nazwa}: ").replace(',', '.'))  # Zamiana ewentualnego przecinka na kropkę
            if warunek is not None and not warunek(liczba):
                raise ValueError
            return liczba
        except ValueError:
            print("Wprowadź poprawną wartość liczbową.")
            if warunek is not None:
                print(f"{nazwa.capitalize()} musi spełniać określony warunek.")

while True:
    # Pobranie danych od użytkownika z zabezpieczeniem
    epsilon = pobierz_liczbe("dokładność (0 < epsilon < 1)", lambda x: 0 < x < 1 and x > 10**(-14))

    x_start_0 = pobierz_liczbe("pierwszy punkt początkowy")
    x_start_1 = pobierz_liczbe("drugi punkt początkowy (różny od pierwszego)", lambda x: x != x_start_0)

    # Sprawdzenie, który punkt początkowy jest mniejszy i przypisanie do zmiennych x_start_0 i x_start_1
    if x_start_0 > x_start_1:
        x_start_0, x_start_1 = x_start_1, x_start_0

    # Wywołanie metody siecznych
    wynik, iteracja = metoda_siecznych(funkcja1, x_start_0, x_start_1, epsilon)
    print(f"Ostateczny wynik: x = {wynik} osiągnięty w iteracji {iteracja}")

    # Pytanie użytkownika o ponowne wykonanie zadania
    decyzja = input("Czy chcesz wykonać ponownie? (Tak/Nie): ")
    if decyzja.lower() == 'tak':
        continue
    elif decyzja.lower() == 'nie':
        break