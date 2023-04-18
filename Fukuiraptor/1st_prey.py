# Homework 6 by N.Rudakov
# Task 30

# import random
import os
os.system('cls')

a1 = int(input("Enter progression 1st element: "))
d = int(input("Enter element difference: "))
quantity = int(input("Enter progression element quantity: "))
progression = []

for i in range(1, quantity):
    an = a1 + (i - 1) * d
    progression.append(an)

print(progression)
