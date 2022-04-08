class Employee:
    """
    represents an employee with a name, salary, birthday, and ID
    """
    def __init__(self, id, name):
    """
    constructs an employee
    """
        self.id = id
        self.name = name
        self.salary = 0
        self.birthday = ''

    #methods

    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary
    def get_birthday(self):
        return self.birthday
    def set_birthday(self, birthday):
        self.birthday = __parse_birthday(birthday)

    def __parse_birthday(self, birthday):  # __ double underscore means the method is private
        if birthday.find('/')<0:
            self.birthday = birthday
        else:
            month, day, year = birthday.split('/')
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            month = months[int(month)-1]
            birthday = "{0} {1}, {2}".format(month, day, year)
            self.birthday = birthday