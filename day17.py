class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

inventory = []

product1 = Product("Laptop", 50000, 10)

inventory.append(product1)

print("Product Added")

for product in inventory:
    print(product.name, product.price, product.quantity)

inventory[0].quantity = 15

print(inventory[0].quantity)

inventory[0].price = 48000

print(inventory[0].price)

new_name = "Laptop"

found = False

for product in inventory:
    if product.name == new_name:
        found = True

if found:
    print("Product already exists")
else:
    inventory.append(Product(new_name, 50000, 5))

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

inventory = []

inventory.append(Product("Laptop", 50000, 10))
inventory.append(Product("Mouse", 800, 25))

inventory[0].quantity = 15

for product in inventory:
    print(product.name, product.price, product.quantity)

