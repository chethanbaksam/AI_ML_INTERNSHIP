class Product:
    def __init__(self, name, price, quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity

inventory = []

inventory.append(Product("laptop", 50000, 10))
inventory.append(Product("Mouse", 800, 25))

product_name = "Laptop"
sell_qty = 3

for product in inventory:
    if product.name == product_name:
        if product.quantity >= sell_qty:
            product.quantity -= sell_qty
        print("Sale Successful")
    else:
        print("Not enough stock")

for product in inventory:
    print(product.name, "- Stock", product.quantity)

product_name = "Mouse"
sell_qty = 30

for product in inventory:
    if product.name == product_name:
        if product.quantity >= sell_qty:
           product.quantity -= sell_qty 
           print("Sale Successful")
        else:
            print("Insufficient Stock")