from project_sixth.car.muscle_car import MuscleCar
from project_sixth.car.sports_car import SportsCar
from project_sixth.driver import Driver
from project_sixth.race import Race


class Controller:
    def __init__(self):
        # lists of objects
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        available_models = [x for x in self.cars if x.model]
        if model in available_models:
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
            self.cars.append(new_car)
        elif car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if driver_name not in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")

        available_cars = [x for x in self.cars if not x.is_taken]

        if car_type not in [x.__class__.__name__ for x in available_cars]:
            raise Exception(f"Car {car_type} could not be found!")

        current_driver = self.find_and_return_driver_by_name(driver_name)
        potential_car = available_cars[-1]

        if current_driver and current_driver.car is True:
            current_model = current_driver.car.model
            potential_car.is_taken = True
            current_driver.car.is_taken = False
            return f"Driver {driver_name} changed his car from {current_model} to {potential_car.model}."

        current_driver.car = potential_car
        potential_car.is_taken = True
        return f"Driver {driver_name} chose the car {potential_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if race_name not in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} could not be found!")

        if driver_name not in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")

        current_driver = self.find_and_return_driver_by_name(driver_name)

        if current_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for race in self.races:
            if driver_name in race.get_drivers_names():
                return f"Driver {driver_name} is already added in {race_name} race."

        current_race = self.find_and_return_race_by_name(race_name)
        current_race.drivers.append(current_driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if race_name not in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} could not be found!")

        current_race = self.find_and_return_race_by_name(race_name)

        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        participants = current_race.drivers

    def find_and_return_driver_by_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver
        return None

    def find_and_return_race_by_name(self, name):
        for race in self.races:
            if race.name == name:
                return race
        return None
