# Homework 3 by N.Rudakov
# Task 16

import os
import random
os.system('cls')

array_size = int(input("Enter list size: "))
tested_array = [random.randint(1, 5) for _ in range(array_size)]
print(tested_array)


def find_index():
    searched_number = int(input("Enter searched value: "))
    counter = 0
    index_list = ''
    index = 0
    for i in tested_array:
        if i == searched_number:
            counter += 1
            index_list += str(index) + ' '
        index += 1
    if counter == 0:
        return print("There is no such element in list")
    print(f"We found {counter} elements, at {index_list}indexes")


find_index()
