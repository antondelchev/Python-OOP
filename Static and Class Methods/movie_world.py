from project.customer_first import CustomerFirst
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: CustomerFirst):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.age_restriction > customer.age and dvd.id == dvd_id:
                        return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                    if dvd.id == dvd_id and dvd not in customer.rented_dvds:
                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"
                    if dvd.is_rented and dvd_id == dvd.id:
                        return "DVD is already rented"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = "\n".join([str(el) for el in self.customers])
        result += "\n"
        result += "\n".join([str(el) for el in self.dvds])

        return result
