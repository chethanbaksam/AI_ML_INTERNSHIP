choice = "yes"

while choice == "yes":
    print("Hii Chethen!")
    choice = input("Type yes to continue: ")

print("What is your favourite fruit, Chethan?")
print("1. Apple")
print("2. Banana")
print("3. Mango")

choice = input("Enter your Choice: ")

if choice == "1":
    print("You have chosen Apple")

elif choice == "2":
    print("You have chosen Banana")

elif choice == "3":
    print("You have chosen Mango")

else:
    print("Invalid choice")


print("Menu:")
print("1. Dosa")
print("2. Idli")
print("3. Upma")
print("4. Pulao")
print("5. Puri")

choice = input("Enter your choice: ")

if choice == "1":
    print("Dosa done!")

elif choice == "2":
    print("Idli done!")

elif choice == "3":
    print("Upma done!")

elif choice == "4":
    print("Pulao done!")

elif choice == "5":
    print("Puri done!")

else:
    print("That's all we have, Chethan!")

while True:

    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice not in ["1", "2", "3"]:
        print("Please enter a valid option")
        continue

    if choice == "3":
        print("Calculator Closed")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print("Answer =", num1 + num2)

    elif choice == "2":
        print("Answer =", num1 - num2)







