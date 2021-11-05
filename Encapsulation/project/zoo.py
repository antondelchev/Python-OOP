from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = int(budget)
        self.__animal_capacity = int(animal_capacity)
        self.__workers_capacity = int(workers_capacity)
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price <= self.__budget and self.__animal_capacity - 1 >= 0:
            self.__budget -= price
            self.__animal_capacity -= 1
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if price > self.__budget and self.__animal_capacity - 1 >= 0:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity - 1 >= 0:
            self.__workers_capacity -= 1
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_animals = 0
        for animal in self.animals:
            tending_animals += animal.money_for_care
        if tending_animals <= self.__budget:
            self.__budget -= tending_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += int(amount)

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        animal_types = {"Lion": [],
                        "Tiger": [],
                        "Cheetah": [],
                        }

        for animal in self.animals:
            animal_types[animal.__class__.__name__].append(animal)

        for animal, animal_name in animal_types.items():
            if animal:
                result += "\n"
                result += f"----- {len(animal_types[animal])} {animal}s:\n"
                result += "\n".join([f"{x.__repr__()}" for x in animal_types[animal]])

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"

        worker_types = {"Keeper": [],
                        "Caretaker": [],
                        "Vet": [],
                        }

        for worker in self.workers:
            worker_types[worker.__class__.__name__].append(worker)

        for worker, worker_name in worker_types.items():
            if worker:
                result += "\n"
                result += f"----- {len(worker_types[worker])} {worker}s:\n"
                result += "\n".join([f"{x.__repr__()}" for x in worker_types[worker]])

        return result
