from project_need_for_speed.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 8
