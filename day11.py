class Student:
    pass

s1 = Student()

print(s1)

class Student:
    pass

s1 = Student()

s1.name = "Chethan"
s1.age = 19

print(s1.name)
print(s1.age)

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Chethan", 19)
s2 = Student("Rahul", 20)
s1.display()
s2.display()

print()

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.city = "Banglore"

    def display(self):
        print("Student:", self.name)
        print("Course:", self.course)
        print("City:", self.city)

student1 = Student("Chethan", "AI & ML")

student1.display()

print()

class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def show(self):
        print("Employee:", self.name)
        print("Department:", self.department)
        print("Salary", self.salary)

e1 = Employee("Chethan", "Data science", "50000")
e2 = Employee("Rahul", "AI", "40000")
e3 = Employee("Mahesh", "ML", "30000")

e1.show()
print()
e2.show()
print()
e3.show()

