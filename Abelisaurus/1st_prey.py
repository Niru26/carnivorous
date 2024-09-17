# Homework 1 by N.Rudakov
# Task 2
import os
os.system('cls')

initial_number = int(input("Enter number: "))
digits_sum = 0

while (initial_number > 0):

    term = initial_number % 10
    initial_number //= 10
    digits_sum += term

print(f"Result: {digits_sum}")
