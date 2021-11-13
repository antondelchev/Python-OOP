from abc import ABC, abstractmethod

from project.animals.animal import Animal
from project.food import Food


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @staticmethod
    def feed(food: Food):
        pass

    def __repr__(self):
        return "{AnimalType} [{AnimalName}, {WingSize}, {AnimalWeight}, {FoodEaten}]"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"
