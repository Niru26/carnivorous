# Homework 1 by N.Rudakov
# Task 8
import os
os.system('cls')

n = int(input("Enter m "))
m = int(input("Enter n "))
k = int(input("Enter k "))
trigger = True

while trigger:
    if m == 0 or n == 0 or k == 0:
        print("Enter valid data.")
        n = int(input("Enter m "))
        m = int(input("Enter n "))
        k = int(input("Enter k "))
    else:
        if (k >= n or k >= m) and (k % m == 0 or k % n == 0) and (m != 1 and n != 1):
            print("Yes, you can!")
        else:
            print("Can't break into two pieces")

    trigger = False