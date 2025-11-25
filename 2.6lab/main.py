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

import geometry

radius = 5
angle = 90

print(f"{radius}")
print(f"{angle}")

area = geometry.circle_area(radius)
print(f"{area:.2f}")

circum = geometry.circumference(radius)
print(f"{circum:.2f}")

sector_area_val = geometry.sector_area(radius, angle)
print(f"({angle}°): {sector_area_val:.2f}")

square_perimeter = geometry.inscribed_square_perimeter(radius)
print(f"{square_perimeter:.2f}")
