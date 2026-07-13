student = {
    "name": "Chethan",
    "age": 18,
    "course": "BBA AI"
}

print(student)
print(student["name"])

student["city"] = "Bangalore"
print(student)

print(student.get("name"))
print(student.get("phone"))
print(student.keys())
print(student.values())

fruits = {"apple", "banana", "apple", "mango"}

print(fruits)

fruits.add("orange")

print(fruits)

set1 = {"apple", "banana", "mango"}
set2 = {"banana", "orange", "mango"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

contacts = {
    "Chethan": "9988776655",
    "Shalini": "4433221100",
    "Aravind": "0987654321"
}

name = input(("Enter name:"))
print(contacts.get(name, "Not found"))
