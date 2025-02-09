class Employee:
    def __init__(self, name, phone, bday, email, position):
        self.__name = name
        self.__phone = phone
        self.__bday = bday
        self.__email = email
        self.__position = position

    def calculate_age(self):
        from datetime import date

        today = date.today()
        age = today.year - self.__bday.year - ((today.month, today.day) < (self.__bday.month, self.__bday.day))
        return age

    def _calculate_salary(self):
        raise NotImplementedError("Subclasses should implement this method")

    # Getters and setters using property
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    name = property(get_name, set_name)

    def get_phone(self):
        return self.__phone

    def set_phone(self, value):
        self.__phone = value

    phone = property(get_phone, set_phone)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def bday(self):
        return self.__bday

    @bday.setter
    def bday(self, value):
        self.__bday = value
