import json

class Student:

    def __init__(self, name, roll, grade):
        self.name = name
        self.roll = roll
        self.grade = grade

students = []

name = input("Enter Name: ")
roll = input("Enter Roll: ")
grade = input("Enter Grade: ")

student = Student(name, roll, grade)

students.append(student)

print("Student Added")

for s in students:
    print(s.name, s.roll, s.grade)

roll = input("Enter Roll to Update: ")

for s in students:
    if s.roll == roll:
        s.grade = input("Enter New Grade: ")

roll = input("Enter Roll to Delete: ")

for s in students:
    if s.roll == roll:
        students.remove(s)
        print("Deleted")

data = []

for s in students:
    data.append({
        "name": s.name,
        "roll": s.roll,
        "grade": s.grade
    })

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print("Saved")

try:

    with open("students.json", "r") as file:

        data = json.load(file)

        print(data)

except FileNotFoundError:

    print("File not found")

