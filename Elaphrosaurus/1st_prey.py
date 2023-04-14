# Homework 5 by N.Rudakov
# Task 26

# import random
import os
os.system('cls')

number_A = int(input("Enter number A: "))
number_B = int(input("Enter number B: "))


def exponentiation(x, y):
    if y == 0:
        return 1

    return exponentiation(x, y - 1) * x


result = exponentiation(number_A, number_B)
print(result)
