def greet():
    print("Hii Chethan!!")

greet()

def greet(name):
    print("Hello", name)

greet("Chethan")
greet("Shalini")
greet("Aravind")

def add(a, b):
    print(a+b)

add(10, 5)
add(20, 30)

def add(a, b):
    return a + b

def subtract(a, b):
    return(a - b)

num1 = int(input("Enter First number: "))
num2 = int(input("Enter second number: "))

print("Addition =", add(num1, num2))
print("subtraction =", subtract(num1, num2))

def square(num):
    return num * num

print(square(5))

def check(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
check(8)

def largest(a, b):
    if a > b:
        return a
    return b

print(largest(10, 20))

def area(length, width):
    return length * width

print(area(10, 5))

