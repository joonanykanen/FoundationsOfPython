# Basic program created to solve
# the computer science problem e2_5 by Joona Nykänen.

import sys
from math import floor

def Alg(A, B):
    value = 0
    if B%2 != 0:
        value = value + A
    print(f"\nStart point when A is '{A}' and\nB is '{B}', value is currently '{value}'!\n")
    while(True):
        B = float(B)
        if round(B) == 1:
            return value
        A = A*2
        B = B/2
        B = floor(B)  # Rounds downwards.
        if B%2 != 0.0:
            value = value + A
            print(f"A is '{A}' and B is '{B}', value is '{value}'!")
        else:
            print(f"A is '{A}' and B is '{B}'. [ -- this part not counted -- ]")

def Main():
    value_M = int(input("Value M: "))
    value_N = int(input("Value N: "))
    bin_check = input("Are you inputting values in bits or decimals?\n(bit=1, decimal=[other]): " )
    if bin_check == "1":
        value_A = bin(Alg(value_M, value_N))
    else:
        value_A = Alg(value_M, value_N)
    print(f"\nThe returned value of A is '{value_A}'.")
    return None

Main()