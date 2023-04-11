# Homework 4 by N.Rudakov
# Task 24

import random
import os
os.system('cls')

gurden_beds_number = int(input())
berries_garden_bed = []
for i in range(gurden_beds_number):
    berries = random.randint(1, 10)
    berries_garden_bed.append(berries)

print("Initial array:", berries_garden_bed)
collected_berries = []
for i in range(len(berries_garden_bed) - 1):
    collected_berries.append(
        berries_garden_bed[i - 1] + berries_garden_bed[i] + berries_garden_bed[i + 1])

print("Mean array:", collected_berries)
collected_berries.append(
    berries_garden_bed[-2] + berries_garden_bed[-1] + berries_garden_bed[0])
print("Final array:", collected_berries)
print("Answer:", max(collected_berries))
