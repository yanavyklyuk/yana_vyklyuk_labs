class Specialization:
    def __init__(self, id, specialization_name):
        self.__id = id
        self.specialization_name = specialization_name

    @property
    def id(self):
        return self.__id