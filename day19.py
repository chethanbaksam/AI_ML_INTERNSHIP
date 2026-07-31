import json

inventory = [
    {"name": "Laptop", "price": 50000, "quantity": 10},
    {"name": "Mouse", "price": 800, "quantity": 25}
]

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

print("Inventory Saved")

with open("inventory.json", "r") as file:
    data = json.load(file)

print(data)

qty = int(input("Enter quantity: "))

if qty > 0:
    print("Valid Quantity")
else:
    print("Invalid Quantity")

with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Loaded Inventory:")
print(inventory)

inventory.append({
    "name": "Keyboard",
    "price": 1500,s
    "quantity": 8
})

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

print("New Product Saved")

