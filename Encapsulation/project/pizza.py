from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = int(toppings_capacity)
        self.toppings = {}

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = value

    @property
    def dough(self):
        return

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        else:
            self.__dough = value

    @property
    def toppings_capacity(self):
        return

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        else:
            self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        for type_name, weight in self.toppings.items():
            if topping.topping_type == type_name and topping.weight:
                self.toppings[type_name] += float(weight)
                return

        if not self.toppings.get(topping.topping_type) and self.toppings_capacity == 0:
            raise ValueError("Not enough space for another topping")

        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        pass
