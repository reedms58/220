"""
Name: <Maddie Reed>
<hw3.py>

Problem: <This program calculates average grades, adds up tips, approximates square roots,
gives a certain number of terms in a sequence, and estimates pi.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Alex Groves
"""


def average():
    acc = 0
    number_of_grades = eval(input("how many grades will you enter? "))
    for i in range(number_of_grades):
        grades = eval(input("Enter grade: "))
        acc = grades + acc
    final_grade = acc / number_of_grades
    print("average is ", final_grade)


def tip_jar():
    total_tips = 0
    for i in range(5):
        tip = eval(input("how much would you like to donate? "))
        total_tips = tip + total_tips
    print("total tips: ", total_tips)


def newton():
    number = eval(input("What number do you want to square root? "))
    times_approximated = eval(input("How many times should we improve the approximation? "))
    approx = 1
    for i in range(times_approximated):
        approx = (number / approx + approx) / 2
    print("the square root is approximately", approx)


def sequence():
    terms = eval(input("how many terms would you like? "))
    for i in range(1, terms + 1):
        sort_terms = i % 2
        sort_terms = sort_terms * 2
        print(sort_terms)

sequence()

def pi():
    terms = eval(input("How many terms in the series? "))
    estimation = 1
    for i in range(1, terms):
        numerator = 2 * i
        print(numerator)
        denominator = 2 * i - 1
        print(denominator)
        estimation = estimation * (numerator * numerator) / (denominator * (denominator + 2))
    print(estimation * 2)


if __name__ == '__main__':
    pass
