"""
Name: Maddie Reed
sales_person.py

Problem: This program forms a class that creates a sales person object with an ID, name, and sales.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:

    def __init__(self, employee_id, name, sales):
        self.employee_id = employee_id
        self.name = name
        self.sales = sales

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() < other.total_sales():
            return -1
        elif self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())

