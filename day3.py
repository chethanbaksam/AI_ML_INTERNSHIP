age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")

age = 20

if age >= 21:
    print("you are eligible")
else:
    print("you are not eligible")

for i in range(5):
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)

    count = 0

for num in range(1, 11):
    if num % 2 == 0:
        print(num)
        count += 1

print("Total even numbers:", count)


grade = int(input("Enter your grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
        print("B")
elif grade >= 70:
        print("C")
elif grade >= 60:
        print("D")
elif grade >= 50:
        print("E")
elif grade < 50:
        print("F")

