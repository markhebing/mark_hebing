x = input("Enter a number: ")
y = 1
count = 0

while y <= int(x):
    if int(x) % y == 0:
        print("Divisible by " + str(y) + "...")
        count = count + 1
    y = y + 1

if count == 2:
    print("Otherwise indivisible...this IS a prime number!")
elif count > 2:
    print("As you can see...this is NOT a prime number.")
