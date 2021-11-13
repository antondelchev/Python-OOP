from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0
