from abc import ABC, abstractmethod

from project_third.decoration.base_decoration import BaseDecoration
from project_third.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []  # list of objects
        self.fish = []  # list of objects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "".strip():
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total_comfort = 0

        for el in self.decorations:
            total_comfort += el.comfort

        return total_comfort

    def add_fish(self, fish: BaseFish):
        if len(self.fish) + 1 > self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ == "FreshwaterFish" or fish.__class__.__name__ == "SaltwaterFish":
            self.fish.append(fish)
            return "Successfully added {fish_type} to {aquarium_name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        fish_info = [el.name for el in self.fish]
        result += f"Fish: {' '.join(fish_info)}\n" if fish_info else "Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result
