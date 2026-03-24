class Product:
    def __init__(self, product, value):
        self.product = product
        self.value = value
    def __str__(self):
        return self.product, self.value
    def get_information(self):
        print(f"Product: {self.product} | Price: {self.value}")

class Client(Product):
    def __init__(self, product, value, name, email, cart):
        super().__init__(product, value)
        self.name = name
        self.email = email
        self.cart = cart
    def __str__(self):
        return self.name, self.email, self.cart
    def
s = Product("Tomato", 9)
print(s.get_information())