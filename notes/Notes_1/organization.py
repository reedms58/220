class Organization:
    def __init__(self, name):
        self.name = name
        self.employees =[]

    def get_name(self):
        return self.name

    def add_employee(self, employee):
