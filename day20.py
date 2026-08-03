import json

try:
    with open("inventory.json", "r") as file:
        inventory = json.load(file)
except:
    inventory = []

name = input("Enter product name: ")

found = False

for product in inventory:
    if product["name"] == name:
        found = True

if found:
    print("Product already exists")
else:
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    print("Product Added")

name = input("Enter product name: ")

for product in inventory:
    if product["name"] == name:
        product["price"] = int(input("New Price: "))
        product["quantity"] = int(input("New Quantity: "))
        print("Product Updated")

name = input("Enter product name: ")
qty = int(input("Enter quantity to sell: "))

for product in inventory:
    if product["name"] == name:
        if product["quantity"] >= qty:
            product["quantity"] -= qty
            print("Sale Successful")
            print("Current Stock:", product["quantity"])
        else:
            print("Insufficient Stock")

for product in inventory:
    print(product["name"], product["price"], product["quantity"])

price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))

if price <= 0 or quantity <= 0:
    print("Invalid Input")
else:
    print("Valid Input")

