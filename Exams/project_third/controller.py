from project_third.aquarium.freshwater_aquarium import FreshwaterAquarium
from project_third.aquarium.saltwater_aquarium import SaltwaterAquarium
from project_third.decoration.decoration_repository import DecorationRepository
from project_third.decoration.ornament import Ornament
from project_third.decoration.plant import Plant
from project_third.fish.freshwater_fish import FreshwaterFish
from project_third.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decoration_repository = DecorationRepository()
        self.aquarium_list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            new_aquarium = FreshwaterAquarium(aquarium_name)
            self.aquarium_list.append(new_aquarium)

        elif aquarium_type == "SaltwaterAquarium":
            new_aquarium = SaltwaterAquarium(aquarium_name)
            self.aquarium_list.append(new_aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decoration_repository.add(decoration)

        elif decoration_type == "Plant":
            decoration = Plant()
            self.decoration_repository.add(decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [x for x in self.aquarium_list if x.name == aquarium_name]
        decoration = self.decoration_repository.find_by_type(decoration_type)

        if not decoration:
            return "There isn't a decoration of type {decoration_type}."

        if aquarium and decoration:
            aquarium[0].add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        aquarium = [x for x in self.aquarium_list if x.name == aquarium_name]
        if len(aquarium[0].fish) + 1 > aquarium[0].capacity:
            return "Not enough capacity."

        if fish_type == "FreshwaterFish" and "Freshwater" not in aquarium[0].__class__.__name__:
            return "Water not suitable."

        if fish_type == "SaltwaterFish" and "Saltwater" not in aquarium[0].__class__.__name__:
            return "Water not suitable."

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
            aquarium[0].add_fish(fish)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)
            aquarium[0].add_fish(fish)

        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = [x for x in self.aquarium_list if x.name == aquarium_name]
        aquarium[0].feed()
        return f"Fish fed: {len(aquarium[0].fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [x for x in self.aquarium_list if x.name == aquarium_name]
        fish_value = sum([x.price for x in aquarium[0].fish])
        decorations_value = sum([x.price for x in aquarium[0].decorations])

        return f"The value of Aquarium {aquarium_name} is {(fish_value + decorations_value):.2f}."

    def report(self):
        result = [str(x) for x in self.aquarium_list]
        return "\n".join(result)
