"""
Name: Maddie Reed
hw10.py

Problem: This program runs the fibonacci sequence, calculates the time it takes to double an investment,
runs the syracuse sequence, and the Goldbach conjecture.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(place):
    num_list = [1, 1]
    loop = 0
    if place < 1:
        return None
    while len(num_list) != place:
        new_num = num_list[loop] + num_list[loop + 1]
        num_list.append(new_num)
        loop += 1
    return num_list[place - 1]


def double_investment(principle, rate):
    annual_total = principle * (1 + rate)
    double_total = annual_total * 2
    years = 0
    while annual_total <= double_total:
        annual_total *= (1 + rate)
        years += 1
    return years


def syracuse(num):
    num_list = [num]
    while num != 1:
        if num % 2 == 0:
            num = num/2
            num_list.append(num)
        else:
            num = 3 * num + 1
            num_list.append(num)
    return num_list


def goldbach(num):
    if num % 2 == 0:
        primes = []
        integer = 1
        while integer < num:
            integer += 1
            number = 0
            factors = 0
            while integer > number:
                number += 1
                if integer % number == 0:
                    factors += 1
            if factors <= 2:
                primes += [integer]
        start_index = 0
        end_index = len(primes) - 1
        prime_1 = primes[start_index]
        prime_2 = primes[end_index]
        total = prime_1 + prime_2
        while total != num:
            total = prime_1 + prime_2
            prime_1 = primes[start_index]
            start_index += 1
            end_index = len(primes) - 1
            prime_2 = primes[end_index]
            while 2 < prime_2 < num:
                prime_2 = primes[end_index]
                end_index -= 1
                total = prime_1 + prime_2
                if total == num:
                    return [prime_1, prime_2]
    else:
        return None


goldbach(1596)
