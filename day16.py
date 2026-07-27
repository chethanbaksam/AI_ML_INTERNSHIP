class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product1 = Product("Laptop", 50000, 10)

product2 = Product("Mouse", 800, 25)

print(product1.name)
print(product1.price)
print(product1.quantity)

products = []

products.append(product1)
products.append(product2)

print(products)

for product in products:
    print(product.name, product.price, product.quantity)

product1.quantity = 8

print(product1.quantity)

products.remove(product2)

print(len(products))

