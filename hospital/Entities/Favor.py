class Favor:
    def __init__(self, favor_name, cost):
        self.__favor_name = favor_name
        if not self.is_valid_cost(cost):
            raise ValueError("Cost must be greater than or equal to 0")
        self.__cost = cost

    @property
    def favor_name(self):
        return self.__favor_name

    @property
    def cost(self):
        return self.__cost

    @staticmethod
    def is_valid_cost(cost):
        return cost >= 0