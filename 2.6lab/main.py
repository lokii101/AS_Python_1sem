from geometry import *

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
