from math import pi


def volume_of_a_spherical_shell(r1, r2):
    volume = (4/3 * pi * r1**3) - (4/3 * pi * r2**3)
    print(abs(round(volume, 3)))


volume_of_a_spherical_shell(3, 3)
volume_of_a_spherical_shell(7, 2)
volume_of_a_spherical_shell(3, 800)
