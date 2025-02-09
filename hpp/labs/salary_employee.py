from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, phone, email, position, bday, salary):
        super().__init__(name, phone, email, position, bday)
        self.__salary = salary

    def calculate_salary(self):
        return self.__salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value
