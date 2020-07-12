number = int(input("Enter a number: "))
x = number

while x > 0:
    if (number % x) == 0:
        print(x)
    x = x-1
