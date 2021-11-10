from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        for el in self.customers:
            if el.name == customer.name:
                return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        for el in self.trainers:
            if el.name == trainer.name:
                return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        for el in self.equipment:
            if el.name == equipment.name:
                return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        for el in self.plans:
            if el.id == plan.id:
                return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        for el in self.subscriptions:
            if el.id == subscription.id:
                return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = [str(x) for x in self.subscriptions if x.id == subscription_id]
        result += [str(x) for x in self.customers if x.id == subscription_id]
        result += [str(x) for x in self.trainers if x.id == subscription_id]
        result += [str(x) for x in self.equipment if x.id == subscription_id]
        result += [str(x) for x in self.plans if x.id == subscription_id]

        return '\n'.join(result)
