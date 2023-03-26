# Homework 2 by N.Rudakov
# Task 14

import os
os.system('cls')

limit = int(input())

for i in range(limit):
    number = 2 ** i
    if number < limit:
        print(number)
