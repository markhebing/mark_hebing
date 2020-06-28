a = [1, 1, 2, 3, 5, 7, 8, 9, 10, 13, 16, 21, 34, 35, 55, 56, 57, 58, 59, 89, 99, 99, 100, 101]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 35, 55, 56, 59, 89, 99, 100, 101]
c = []

if len(a) > len(b):
    x = len(a) - 1
    while x >= 0:
        if a[x] in b:
            c.append(a[x])
        x = x - 1

if len(b) > len(a):
    x = len(b) - 1
    while x >= 0:
        if b[x] in a:
            c.append(b[x])
        x = x - 1

c = list(dict.fromkeys(c))
c.reverse()
print(c)
