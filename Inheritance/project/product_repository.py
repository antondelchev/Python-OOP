from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        for item in self.products:
            if item.name == product.name:
                item.quantity += int(product.quantity)
                return

        self.products.append(product)

    def find(self, product_name):
        for item in self.products:
            if item.name == product_name:
                return item

    def remove(self, product_name):
        for item in self.products:
            if item.name == product_name:
                self.products.remove(item)

    def __repr__(self):
        result = [f"{product.name}: {product.quantity}" for product in self.products]
        return "\n".join(result)
