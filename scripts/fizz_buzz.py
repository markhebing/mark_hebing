def fizz_buzz(x):
    if x % 3 == 0 and x % 5 != 0:
        print("\"Fizz\"")
    elif x % 3 != 0 and x % 5 == 0:
        print("\"Buzz\"")
    elif x % 3 == 0 and x % 5 == 0:
        print("\"FizzBuzz\"")
    elif x % 3 != 0 and x % 5 != 0:
        print("\"" + str(x) + "\"")


fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(4)
