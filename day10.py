contacts = {}

contacts["Chethan"] = "9876543210"
contacts["Rahul"] = "9998887776"

print(contacts)

contacts["Chethan"] = "1234567890"

print(contacts)

del contacts["Rahul"]

print(contacts)

name = "Chethan"

if name in contacts:
    print("Found")
else:
    print("Not Found")

contacts = {}

while True:

    print("\n1.Add")
    print("2.View")
    print("3.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        contacts[name] = phone

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        break

