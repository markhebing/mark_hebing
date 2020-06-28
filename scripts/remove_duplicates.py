a = [1, 1, 2, 3, 5, 7, 7, 7, 7, 8, 9, 10, 13, 13, 13, 13, 13, 16, 21, 21, 21, 22, 34, 35, 55, 56, 57, 58, 59, 89, 99, 99, 100, 101, 102, 345, 456, 567, 678, 789, 890, 1000]
b = []
c = len(a)


def reduction_function():
    x = 0
    while x < c:
        if a[x] not in b:
            b.append(a[x])
        x = x + 1
    print(b)


reduction_function()
