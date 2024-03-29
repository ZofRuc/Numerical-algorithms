# -*- coding: utf-8 -*-
"""Projekt_AN1_ŚA_RZ.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15kSIHVgrKpPGhNaPoDikZWjRAZvP5jQY
"""

def lagrange_interpolation(x, y, t):
    n = len(x)
    result = 0.0

    for j in range(n):
        L = 1.0
        for i in range(n):
            if i != j:
                L *= (t - x[i]) / (x[j] - x[i])
        result += y[j] * L

    return result

def general_lagrange_polynomial(x):
    n = len(x)
    polynomial = "P(x) = "
    for j in range(n):
        term = f"{x[j]:.4f}"
        for i in range(n):
            if i != j:
                term = f"{term} * (x - {x[i]:.4f})"
        if j > 0:
            polynomial += " + "
        polynomial += term

    return polynomial

# Wczytywanie liczby naturalnej n
while True:
    try:
        n = int(input("Podaj liczbę węzłów (n): "))
        if n > 0:
            break
        else:
            print("Podaj liczbę naturalną (n > 0)!")
    except ValueError:
        print("Podaj liczbę naturalną (n > 0)!")

x = []
y = []
for i in range(n):
    while True:
        try:
            x_i = float(input(f"Podaj x_{i}: "))
            y_i = float(input(f"Podaj y_{i}: "))
            x.append(x_i)
            y.append(y_i)
            break
        except ValueError:
            print("Wprowad liczbę!")

print("Wielomian interpolacyjny w postaci Lagrange'a:")
interpolation_polynomial = general_lagrange_polynomial(x)
#print(interpolation_polynomial)
print(f"P(x) = {interpolation_polynomial}")

while True:
    t = float(input("Podaj argument t (lub wpisz -1 aby zakończyć): "))
    if t == -1:
        break
    result = lagrange_interpolation(x, y, t)
    print(f"P({t}) = {result:.4f}")

print(f"P(x) = lagrange_interpolation(x, y, t)")