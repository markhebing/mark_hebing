string = input("Enter a fraction and I will simplify it or type exit: ")

while string != "exit":
    address = string.index("/")
    num1 = string[0:address]
    num2 = string[(address + 1):]
    num1b = int("".join(num1))
    num2b = int("".join(num2))
    if num1b % num2b == 0:
        num_int = int(num1b / num2b)
        print("\"" + string + "\"" + " reduces to " + "\"" + str(num_int) + "\"")
    elif int(num2b) % int(num1b) == 0:
        num2b = int(num2b / num1b)
        num1b = 1
        print("\"" + string + "\"" + " reduces to " + "\"" + str(num1b) + "/" + str(num2b) + "\"")
    elif num1b % num2b != 0 and num2b % num1b != 0 and num1b < num2b:
        for i in range(num1b, 0, -1):
            if i == 1:
                print("\"" + string + "\"" + " reduces to " + "\"" + str(num1b) + "/" + str(num2b) + "\"")
                break
            if num1b % i == 0 and num2b % i == 0:
                num2b = int(num2b / i)
                num1b = int(num1b / i)
                print("\"" + string + "\"" + " reduces to " + "\"" + str(num1b) + "/" + str(num2b) + "\"")
                break
    elif num1b % num2b != 0 and num2b % num1b != 0 and num1b > num2b:
        for i in range(num2b, 0, -1):
            if i == 1:
                print("\"" + string + "\"" + " reduces to " + "\"" + str(num1b) + "/" + str(num2b) + "\"")
                break
            if num1b % i == 0 and num2b % i == 0:
                num2b = int(num2b / i)
                num1b = int(num1b / i)
                print("\"" + string + "\"" + " reduces to " + "\"" + str(num1b) + "/" + str(num2b) + "\"")
                break
    string = input("Enter a fraction and I will simplify it or type exit: ")
