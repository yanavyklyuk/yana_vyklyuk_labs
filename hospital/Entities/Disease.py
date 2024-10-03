class Disease:
    def __init__(self, id, disease_name):
        self.__id = id
        self.__disease_name = disease_name

    @property
    def id(self):
        return self.__id

    @property
    def disease_name(self):
        return self.__disease_name