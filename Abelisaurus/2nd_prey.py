# Homework 1 by N.Rudakov
# Task 4

total_cranes_qty = int(input("Enter paper cranes quantity: "))
flag = True

while flag:
    if total_cranes_qty % 6 != 0:
        print("Wrong data, pls.enter again")
        total_cranes_qty = int(input("Enter paper cranes quantity: "))
    else:
        Peter = total_cranes_qty // 6
        Sergei = total_cranes_qty // 6
        Kate = (total_cranes_qty // 3) * 2
        print(f"Peter - {Peter}, Sergei - {Sergei}, Kate - {Kate}")
        flag = False
