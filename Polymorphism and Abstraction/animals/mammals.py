from abc import ABC, abstractmethod

from project.animals.animal import Animal


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.living_region = living_region


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"
