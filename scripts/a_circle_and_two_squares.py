from math import sqrt


def area_inner_square(r):
    area = (2 * (sqrt(r ** 2 / 2))) ** 2
    return area


print(int(round(area_inner_square(5))))
print(int(round(area_inner_square(6))))
print(int(round(area_inner_square(7))))
