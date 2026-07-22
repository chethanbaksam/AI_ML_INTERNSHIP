file = open("notes.txt", "w")
file.write("Hello Chethan")
file.close()
print("Data Saved")

file = open("notes.txt", "r")
data = file.read()
print(data)
file.close()

file = open("notes.txt", "a")
file.write("Welcome to AI Internship")
file.close()
print("New Data Added")

print()

with open("notes.txt", "r")  as file:
    data = file.read()

print(data)

import json

student = {
    "name": "Chethan",
    "age": 19,
    "course": "AI"
}

print(student)

import json

student = {
    "name": "Chethan",
    "age": 19,
    "course": "AI"
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("JSON Saved")

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)

print()

import json

students = [
    {"name": "Chethan", "age": 19},
    {"name": "Rahul", "age": 20},
    {"name": "Anjali", "age": 18}
]

with open("students.json", "w") as file:
    json.dump(students, file)

with open("students.json", "r") as file:
    data = json.load(file)

for student in data:
    print(student)

print()

import json

name = input("Enter Name: ")
age = int(input("Enter Age: "))

student = {
    "name": name,
    "age": age
}

with open("record.json", "w") as file:
    json.dump(student, file)

print("Student Record Saved")