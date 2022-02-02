"""
Name: <Maddie Reed>
hw3.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
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
    pass


def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    pass
