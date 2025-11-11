Описать функцию RectPS, вычисляющую периметр P и площадь S прямоугольника со сторонами, параллельными осям координат, по координатам (x1,y1), (x2,y2) его противоположных вершин.
def RectPS(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    P = 2 * (width + height)
    S = width * height
    return P, S
P, S = RectPS(1, 1, 4, 5)
print(P,S)
