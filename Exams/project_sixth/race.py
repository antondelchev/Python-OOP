class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []  # list of objects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "".strip():
            raise ValueError("Name cannot be an empty string!")

        self.__name = value

    def get_drivers_names(self):
        return [x.name for x in self.drivers]

    def sort_fastest(self):
        info = []
        for driver in self.drivers:
            info.append({f"{driver.name}": driver.car.MAX_SPEED_LIMIT})
