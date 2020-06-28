random_list = [1, 3, 5, 7, 8, 10, 15, 79, 85, 90, 101, 201, 204, 234, 256, 270, 998]
value = input("Enter and number between 0 and 1000 and A.I. will check to see if it is in the list: ")
value = int(value)

if value in random_list:
    print("True")
else:
    print("False")
