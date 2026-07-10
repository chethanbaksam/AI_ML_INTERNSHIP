fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(fruits[0])
print(fruits[1])

marks = [78, 45, 90, 67, 82]

marks.sort()

print(marks)

fruits = ["Apple", "Banana", "Mango"]

item = input("Enter fruit name: ")

if item in fruits:
    print("Found")
else:
    print("Not Found")

colors = ("Red", "Green", "Blue")

print(colors)
print(colors[0])

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))

marks = []

for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("Marks:", marks)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))