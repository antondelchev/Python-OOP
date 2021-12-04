from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        else:
            self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, value):
        self.oxygen += value

    def __str__(self):
        backpack_info = ', '.join(self.backpack) if self.backpack else "none"
        return f"Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {backpack_info}"
