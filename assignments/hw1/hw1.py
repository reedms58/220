"""
Name: Maddie Reed
hw1.py

Problem: This program calculates the area of a rectangle, the volume of a rectangular prism, percentages,
 coffee prices, and converts kilometers to miles.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length*width
    print("Area=", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length*width*height
    print("Volume=", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    percentage = (shots_made/total_shots)*100
    print("Shooting Percentage: ", percentage, "%")


def coffee():
    pounds_of_coffee = eval(input("How many pounds of coffee would you like? "))
    total = pounds_of_coffee*(10.5+0.86)+1.5
    print("You're total is: ", "$", total)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = kilometers/1.6
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
