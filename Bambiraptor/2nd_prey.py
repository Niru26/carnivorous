# Homework 2 by N.Rudakov
# Task 12

import os
os.system('cls')

S = int(input())
P = int(input())

for i in range(S):
    for j in range(P):
        if i + j == S and i * j == P:
            print(i, j)
