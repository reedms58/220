"""
Name: Maddie Reed
sales_force.py

Problem: This program creates a class that sorts and organizes data related to the SalesPerson
class.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import *


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        for line in lines:
            person = line.split(',')
            employee_id, name, sales = person[0], person[1], person[2].replace("\n", "")
            sales = sales.split()
            for sale in sales:
                index = sales.index(sale)
                sales.pop(index)
                sale = eval(sale)
                sales.insert(index, sale)
            self.sales_people += employee_id, name, sales

    def quota_report(self, quota):
        quota_list = []
        for i in range(0, len(self.sales_people), 3):
            employee_list = []
            person_id = self.sales_people[i]
            name = self.sales_people[i+1]
            sales = self.sales_people[i+2]
            employee = SalesPerson(person_id, name, sales)
            met = employee.met_quota(quota)
            employee_list.append(person_id)
            employee_list.append(name)
            employee_list.append(sales)
            employee_list.append(met)
            quota_list.append(employee_list)
        return quota_list

    def top_seller(self):
        top = [0]
        employee_with_total = []
        for i in range(0, len(self.sales_people), 3):
            employee_list = []
            person_id = self.sales_people[i]
            name = self.sales_people[i + 1]
            sales = self.sales_people[i + 2]
            employee = SalesPerson(person_id, name, sales)
            total_sales = employee.total_sales()
            employee_list.append(person_id)
            employee_list.append(name)
            employee_list.append(sales)
            employee_list.append(total_sales)
            employee_with_total.append(employee_list)
        for i in range(0, len(employee_with_total)):
            maximum = 0
            for person in employee_with_total:
                if person[3] > maximum:
                    maximum = person[3]
                    top = person
                elif person[3] == maximum:
                    top.append(person)
        return top

    def individual_sales(self, employee_id):
        employee = [0]
        for i in range(0, len(self.sales_people), 3):
            if self.sales_people[i] == employee_id:
                employee.pop(0)
                employee.insert(0, self.sales_people[i])
                employee.append(self.sales_people[i + 1])
                employee.append(self.sales_people[i + 2])
                return employee
        if employee[0] == 0:
            return None

    def get_sale_frequencies(self):
        dic = {}
        for i in range(2, len(self.sales_people), 3):
            for k in range(len(self.sales_people[i])):
                sale_list = self.sales_people[i]
                dic[sale_list[k]] = dic.get(sale_list[k], 0) + 1
        return dic

