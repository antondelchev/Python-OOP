from project_first.astronaut.astronaut_repository import AstronautRepository
from project_first.astronaut.biologist import Biologist
from project_first.astronaut.geodesist import Geodesist
from project_first.astronaut.meteorologist import Meteorologist
from project_first.planet.planet import Planet
from project_first.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        new_astronaut = self.create_astronaut(astronaut_type, name)

        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = self.create_planet(name, items)

        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut:
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {name} was retired!"

        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = []
        self.astronaut_repository.astronauts.sort(key=lambda x: x.oxygen, reverse=True)

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30 and len(suitable_astronauts) < 5:
                suitable_astronauts.append(astronaut)

        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        participated_astronauts = []

        for astronaut in suitable_astronauts:
            if len(planet.items) == 0:
                break

            participated_astronauts.append(astronaut)
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        if len(planet.items) == 0:
            self.completed_missions += 1
            return f"Planet: {planet_name} was explored. {len(participated_astronauts)} " \
                   f"astronauts participated in collecting items."
        else:
            self.not_completed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.completed_missions} successful missions!\n" \
                 f"{self.not_completed_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        result += '\n'.join([str(astronaut) for astronaut in self.astronaut_repository.astronauts])
        return result.strip()

    @staticmethod
    def create_astronaut(astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")

    @staticmethod
    def create_planet(name, items):
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        return new_planet
