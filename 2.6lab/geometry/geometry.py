import math

def circle_area(radius):
    if radius < 0:
        raise ValueError()
    return math.pi * radius ** 2


def circumference(radius):
    if radius < 0:
        raise ValueError()
    return 2 * math.pi * radius

def sector_area(radius, angle_degrees):
    if radius < 0:
        raise ValueError()
    if angle_degrees < 0 or angle_degrees > 360:
        raise ValueError()
    return (angle_degrees / 360) * math.pi * radius ** 2

def inscribed_square_perimeter(radius):
    if radius < 0:
        raise ValueError("")
    diagonal = 2 * radius
    side = diagonal / math.sqrt(2)
    return 4 * side
