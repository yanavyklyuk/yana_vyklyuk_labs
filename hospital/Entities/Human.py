import datetime
class Human:
    def __init__(self, id, first_name, last_name, sex, date_of_birth, phone_number):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        if sex.lower() not in ['male', 'female']:
            raise ValueError("There are only two genders: male and female.")
        self._sex = sex.lower()
        if not isinstance(date_of_birth, datetime.date) or date_of_birth > datetime.date.today():
            raise ValueError("Start of work must be a datetime.time object.")
        self.__date_of_birth = date_of_birth
        self.__phone_number = phone_number

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self):
        return (f'First name: {self.__first_name}\nLast name: {self.__last_name}\nSex: {self._sex}\n'
                f'Date of birth: {self.__date_of_birth}\nPhone number: {self.__phone_number}')

    def greet(self):
        return f'Hi, I am a human {self.__first_name} {self.__last_name}'