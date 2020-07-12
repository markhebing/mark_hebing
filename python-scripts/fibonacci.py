i = input("How many Fibonacci numbers would you like to generate? ")
x = 0
y = 1
z = x + y
counter = 3

if int(i) == 0:
    print("0 ... 0")
elif int(i) == 1:
    print("0 ... 0")
    print("1 ... 1")
elif int(i) == 2:
    print("0 ... 0")
    print("1 ... 1")
    print("2 ... 1")
elif int(i) >= 2:
    print("0 ... 0")
    print("1 ... 1")
    print("2 ... 1")
    while counter < (int(i) + 1):
        x = y
        y = z
        z = x + y
        print(str(counter) + " ... " + str(z))
        counter = counter + 1
