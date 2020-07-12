from math import sqrt


def quadratic_equation(a, b, c):
    x1 = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
    print(str(x1) + ", " + str(x2))


quadratic_equation(1, 2, -3)
quadratic_equation(2, -7, 3)
quadratic_equation(1, -12, -28)
