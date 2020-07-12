import random
import time

x = 0
y = input("How many characters would you like your passwords to be? ")

while x < 10:

    pass_word = []
    z = 0
    while z < int(y):
        random_character = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&')
        pass_word.append(random_character)
        z = z + 1
    print(*pass_word, sep='')
    x = x + 1
    time.sleep(.25)
