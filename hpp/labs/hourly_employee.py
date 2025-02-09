from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, phone, email, position, bday, number_of_hours, hourly_pay):
        super().__init__(name, phone, email, position, bday)
        self.__number_of_hours = number_of_hours
        self.__hourly_pay = hourly_pay

    def calculate_salary(self):
        return self.__number_of_hours * self.__hourly_pay

    @property
    def number_of_hours(self):
        return self.__number_of_hours

    @number_of_hours.setter
    def number_of_hours(self, value):
        self.__number_of_hours = value

    @property
    def hourly_pay(self):
        return self.__hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, value):
        self.__hourly_pay = value
