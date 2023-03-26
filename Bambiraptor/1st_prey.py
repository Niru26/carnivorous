# Homework 2 by N.Rudakov
# Task 10

import random
import os
os.system('cls')

coins_qty = int(input())
flipped_coins = [random.randint(0, 1) for _ in range(coins_qty)]
coins_zero_qty = 0
coins_one_qty = 0

for i in range(coins_qty):
    if flipped_coins[i]:
        coins_one_qty += 1
    else:
        coins_zero_qty += 1

print(f"0 - {coins_zero_qty}, 1 - {coins_one_qty}, initial array - {flipped_coins}")
print(coins_zero_qty if coins_one_qty > coins_zero_qty else coins_one_qty)

# print(len(flipped_coins))
# print(flipped_coins)
# print(flipped_coins[5])
