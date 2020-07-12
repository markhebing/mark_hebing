import random
import time

print("\nPick a number between 0 and 100 and I will try to guess it.")
print("\nIf I am high, type \"high\". If I am low, type \"low\". If I guessed correctly, type \"correct\".")

x = random.randint(0, 100)
lower = 0
upper = 100
y = 1

print("\nMy first guess is the number " + str(x))

guess = input("\nAm I high, low, or correct? ")

while guess != str("correct") and lower != upper:

    if guess == str("high") and lower != upper and x != lower and x != upper:
        upper = x - 1
        x = random.randint(lower, upper)
        print("\nHmmm...something between " + str(lower) + " and " + str(upper) + "...")
        time.sleep(2)
        if upper == lower:
            print("\nWhoa! It has to be " + str(x) + "!")
        print("\nOK...Is it " + str(x) + "?")
        y = y + 1
        guess = input("\nAm I high, low, or correct? ")

    elif guess == str("low") and lower != upper and x != lower and x != upper:
        lower = x + 1
        x = random.randint(lower, upper)
        print("\nHmmm...something between " + str(lower) + " and " + str(upper) + "...")
        time.sleep(2)
        if upper == lower:
            print("\nWhoa! It has to be " + str(x) + "!")
        print("\nOK...Is it " + str(x) + "?")
        y = y + 1
        guess = input("\nAm I high, low, or correct? ")

    elif guess != (str("high") and guess != str("low") and guess != str("correct")) and lower != upper and x != lower and x != upper:
        print("\nHmmm...")
        time.sleep(2)
        guess = input("\nI don\'t understand your response. Please tell me if I am \"high\", \"low\" or \"correct\"? ")

if upper == lower:
    print("\nYeah...I know it is " + str(x) + "! LOL!")

print("\nWow! That was tough! It took me " + str(y) + " guesses!")
