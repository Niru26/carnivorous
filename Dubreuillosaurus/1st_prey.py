# Homework 4 by N.Rudakov
# Task 22

import random
import os
os.system('cls')


enter_m_n = [int(x) for x in input("Enter two sets size: ").split()]
n = enter_m_n[0]
m = enter_m_n[1]
print("n and m numbers:", n, m)
set_1_values = [random.randint(1, 10) for _ in range(n)]
set_2_values = [random.randint(1, 10) for _ in range(m)]
print("Generated list one:", set_1_values)
print("Generated list two:", set_2_values)
set_1 = set(set_1_values)
set_2 = set(set_2_values)
sets_union = set_1 | set_2

print("This is set one:", set_1)
print("This is set two:", set_2)
print("Set one and set two union:", sets_union)

reversed_set_list = list(sets_union)[::-1]
print("Reversed union set:", reversed_set_list)
