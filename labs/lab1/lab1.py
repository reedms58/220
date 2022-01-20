"""
Name: Maddie Reed
monthly_interest.py

Problem: This program calculates the monthly interest charged on a credit card.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def monthly_interest():
    annual_interest = eval(input("What is the annual interest rate? as a decimal: "))
    days_in_billing_cycle = eval(input("How many days are in the billing cycle?: "))
    net_balance = eval(input("What was the previous net balance?: "))
    payment_amount = eval(input("How much is the payment amount?: "))
    day_of_payment = eval(input("What day in the billing cycle was the payment made?: "))
    step1 = net_balance*days_in_billing_cycle
    step2 = payment_amount*(days_in_billing_cycle-day_of_payment)
    step3 = step1-step2
    annual_interest = step3/days_in_billing_cycle
    print("$",annual_interest)

monthly_interest()