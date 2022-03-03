"""
Name: Maddie Reed
lab7.py

Problem: This program calculates the weighted grade average of a class
as well as the class average.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    line_list = in_file.readlines()
    class_total = 0
    student_total = 0
    for line in line_list:
        broken_string = line.split(':')
        name = broken_string[0]
        grades = broken_string[1].split()
        grades_len = len(grades)
        grade_groups = grades_len//2
        acc = 0
        weight_acc = 0
        weights = []
        earned_grades = []

        for number in range(0, grades_len, 2):
            weights = weights + [eval(grades[number])]
        for number in range(1, grades_len, 2):
            earned_grades = earned_grades + [eval(grades[number])]
        for number in range(grade_groups):
            product = weights[number] * earned_grades[number]
            weight_acc = weight_acc + weights[number]
            acc = acc + product
        weighted_ave = acc/100

        if weight_acc == 100:
            student_total = student_total + 1
            class_total = class_total + weighted_ave
            print(name + ":", round(weighted_ave, 1), file=out_file)
        elif weight_acc < 100:
            print(name + ":", "Error: The weights are less than 100.", file=out_file)
        elif weight_acc > 100:
            print(name + ":", "Error: The weights are more than 100.", file=out_file)
    class_average = class_total / student_total
    print("Class average: ", class_average, file=out_file)
    in_file.close()
    out_file.close()
