"""
Name: <Maddie Reed>
lab3.py

Problem: This program calculates the average vehicles per day on different roads
and the total vehicles on all roads.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    cars_on_all_roads = 0
    number_of_roads_surveyed = eval(input("How many roads were surveyed? "))
    for i in range(number_of_roads_surveyed):
        print("How many days was road", i + 1, "surveyed? ", end=' ')
        number_of_days_surveyed = eval(input())
        total_cars = 0
        for j in range(number_of_days_surveyed):
            print("\t", "How many cars traveled on day", j + 1, "?", end=' ')
            cars_traveled = eval(input())
            total_cars = cars_traveled + total_cars
        average_car_per_day = total_cars / number_of_days_surveyed
        print("Road", i + 1, "average vehicles per day: ", average_car_per_day)
        cars_on_all_roads = cars_on_all_roads + total_cars
    average_cars_on_all_roads = cars_on_all_roads / number_of_roads_surveyed
    print("Total number of vehicles traveled on all roads: ", cars_on_all_roads)
    print("Average number of vehicles per road: ", round(average_cars_on_all_roads, 2))
