# Homework 5 by N.Rudakov
# Task 28

# import random
import os
os.system('cls')

number_A = int(input("Enter positive number A: "))
number_B = int(input("Enter positive number B: "))


def recursion_summary(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    x += 1
    y -= 1
    if y > 0:
        return recursion_summary(x, y)
    else:
        return x


result = recursion_summary(number_A, number_B)
print(result)
