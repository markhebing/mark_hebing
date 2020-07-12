import random

x = 0
z = random.randrange(1000, 9999, 1)
z = str(z)
cows = 0
bulls = 0
list_generated = [int(i) for i in str(z)]
print(list_generated)

while cows < 4:
    cows = 0
    bulls = 0
    counter = 0
    y = input("Enter a 4 digit number: ")
    y = str(y)
    list_input = [int(i) for i in str(y)]
    while counter < 4:
        if list_input[counter] == list_generated[counter]:
            cows = cows + 1
        if list_input[counter] in list_generated and list_input[counter] != list_generated[counter]:
            bulls = bulls + 1
        counter = counter + 1
    print("cow = " + str(cows) + ", " + "bulls = " + str(bulls))

print("You guessed it! The number is " + str(z))
