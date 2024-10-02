from Entities.Human import Human
class Patient(Human):
    def __init__(self, id, first_name, last_name, sex, date_of_birth, phone_number, country, city, street):
        super().__init__(id,first_name, last_name, sex, date_of_birth, phone_number)
        self.country = country
        self.city = city
        self.street = street

    def greet(self):
        return f'Hi, I am a patient {self.first_name} {self.last_name}'

    def sicken(self):
        return f'My name is {self.first_name} and I am ill('