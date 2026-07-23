
try:
    num = int(input("Enter a number: "))
    result = 100 / num

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Please enter numbers only!")

print()

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input!")

else:
    print("Valid number entered:", num)

print()

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Answer:", num1 / num2)

except ValueError:
    print("Numbers only!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

print()

correct_password = "admin123"

try:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
    else:
        raise ValueError

except ValueError:
    print("Wrong Password")

print()

while True:

    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative.")
            continue

        print("Valid age:", age)
        break

    except ValueError:
        print("Please enter numbers only.")