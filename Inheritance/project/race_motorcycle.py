from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 8
