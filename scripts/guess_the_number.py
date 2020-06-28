import random

x = random.randint(1, 1000)
y = input("Enter a number from 1 to 1000 or type exit to stop: ")
z = 0

while y != x:
    if str(y) == "exit":
        break
    elif int(y) > x:
        print("You guessed too high.")
        z = z + 1
        y = input("Guess again: ")
    elif int(y) < x:
        print("You guessed too low.")
        z = z + 1
        y = input("Guess again: ")
    elif int(y) == x:
        print("Success! It took you " + str(z + 1) + " guesses!")
        y = input("Enter a number from 1 to 1000 or type exit to stop: ")

print("Thanks for playing!")
