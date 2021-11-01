from project.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 3
