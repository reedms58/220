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

a, b, c = eval(input("enter a, b, and c: "))
root_1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
root_2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
print("root 1: ", root_1, "root 2: ", root_2)

age = 3.5
int(age)

round(3.758694, 2)