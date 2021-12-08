from project_third.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    __INITIAL_SIZE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, self.__INITIAL_SIZE, price)

    def eat(self):
        self.size += 3
