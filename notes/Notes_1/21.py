principal = eval(input("enter the account balance: "))
apr = eval(input("enter the annual percentage rate: "))
for _ in range(10):
    principal = principal * (1+apr)
    print(principal)
    print("Your balance after 10 years is", principal)

for i in range(5):
    for j in range(5):
        print(i,j, end="-")

for i in range(100):
    print(i%4)

import math
