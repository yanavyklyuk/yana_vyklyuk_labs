import datetime
from Entities.Human import Human
from Entities.Specialization import Specialization
class Doctor(Human):
    def __init__(self, id, first_name, last_name, sex, date_of_birth, phone_number, specialization, experience):
        if not isinstance(specialization, Specialization):
            raise TypeError("Specialization must be a specialization object.")
        if experience < 0:
            raise ValueError("Experience must be positive.")
        super().__init__(id, first_name, last_name, sex, date_of_birth, phone_number)
        self.specialization = specialization
        self.experience = experience

    def greet(self):
        return f'Hi, I am a doctor {self.first_name} {self.last_name}'

    def treat(self):
        return f'My specialization is {self.specialization.specialization_name}, I work for {self.experience} years. I treat your disease.'