from project_first.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []  # list of objects

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None
