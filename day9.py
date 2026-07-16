name = "cHeThAn"

print(name.upper())
print(name.lower())
print(name.title())

text = "    Hello World    "

print(text.strip())

sentence = "I love Python"

print(sentence.replace("Python", "AI"))

message = "banana"

print(message.count("a"))

text = "Python Programming"

print(text.find("Program"))

filename = "project.py"

print(filename.startswith("project"))
print(filename.endswith(".py"))

sentence = "Python is fun"

words = sentence.split()

print(words)

letters = ["A", "B", "C"]

result = "-".join(letters)

print(result)

name = input("Enter your name: ")

clean_name = name.strip().title()

print("Welcome,", clean_name)
