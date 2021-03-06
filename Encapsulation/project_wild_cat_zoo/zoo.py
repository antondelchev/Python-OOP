class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity + 1 <= self.__animal_capacity:
            return f"{animal} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        pass

    def fire_worker(self, worker_name):
        pass

    def pay_workers(self):
        pass

    def tend_animals(self):
        pass

    def profit(self, amount):
        pass

    def animals_status(self):
        pass
