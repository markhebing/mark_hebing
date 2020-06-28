def factorial(x):
    y = x
    z = 1
    while y != 0:
        z = z * y
        y = y - 1
        print(str(y) + " . . . " + str(z))


number = input("Enter a number...any number: ")

factorial(int(number))
