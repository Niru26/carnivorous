# Homework 6 by N.Rudakov
# Task 30

import random
import os
os.system('cls')


qunaity = int(input("Enter array elements: "))

random_list = [random.randint(-10, 10) for _ in range(qunaity)]
print(random_list)

min_number = int(input("Enter minimum: "))
max_number = int(input("Enter maximum: "))

for index, value in enumerate(random_list):
    if min_number <= value <= max_number:
        print(index, end=' ')
