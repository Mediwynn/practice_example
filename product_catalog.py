class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        tot = self.price * self.quantity
        value = print(f"Total value of stock = {tot}")
        return value