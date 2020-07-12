from math import sqrt


def squares_and_cubes(list_x):
    if (sqrt(list_x[0])**3) == list_x[1]:
        print(True)
    else:
        print(False)


squares_and_cubes([4, 8])
squares_and_cubes([16, 48])
squares_and_cubes([9, 27])
