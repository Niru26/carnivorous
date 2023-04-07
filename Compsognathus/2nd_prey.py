# Homework 3 by N.Rudakov
# Task 18

import os
import random
os.system('cls')

number_n = int(input("Enter quantity of numbers in list: "))
random_array = [random.randint(1, 10) for _ in range(number_n)]
print(random_array)
number_x = int(input("Enter number to check: "))


def make_list_of_differences(array, number):
    difference = []
    for list_item in array:
        difference_current = abs(list_item - number)
        difference.append(difference_current)
    return difference


def get_closest_to_x(array, number):
    list_of_differences = make_list_of_differences(array, number)
    if number > max(array):
        return max(array)
    if number < min(array):
        return min(array)
    index_of_closest_to_x = list_of_differences.index(min(list_of_differences))
    return array[index_of_closest_to_x]


closest_to_x = get_closest_to_x(random_array, number_x)
print("Result:", closest_to_x)
