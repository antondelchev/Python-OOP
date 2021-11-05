class Topping:
    def __init__(self, topping_type, weight):
        self.topping_type = topping_type
        self.weight = float(weight)

    @property
    def topping_type(self):
        return

    @topping_type.setter
    def topping_type(self, value):
        if not value:
            raise ValueError("The topping type cannot be an empty string")
        else:
            self.__topping_type = value

    @property
    def weight(self):
        return

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        else:
            self.__weight = value
