class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)

    def decrease(self, quantity):
        if self.quantity - int(quantity) < 0:
            self.quantity = 0
        else:
            self.quantity -= int(quantity)

    def increase(self, quantity):
        self.quantity += int(quantity)

    def __repr__(self):
        return self.name
