import random

print(random.randint(1, 6))

import random

print(random.random())

import random

fruits = ("apple", "banana", "cherry")
print(random.choice(fruits))

import random

cards = ["A", "K", "Q", "J"]

random.shuffle(cards)

print(cards)

import random

secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct!!")
else:
    print("Incorrect!")
    print("The Number was: ", secret)

import random

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a Number between 1 and 10: "))
    attempts += 1

    if guess == secret:
        print("Your Right!")
        print("Attempts:", attempts)
        break
    else:
        print("Try Again?")