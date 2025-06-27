def linear_coefficients(p1: tuple, p2: tuple):
    x1, y1 = p1
    x2, y2 = p2
    k = (y2 - y1) / (x2 - x1)
    b = (y1 * x2 - x1 * y2) / (x2 - x1)
    return k, b


print(linear_coefficients((1, 2), (2, 3)))

print(linear_coefficients((0, 0), (1, 5)))

print(linear_coefficients((0, 2), (2, 2)))

print(linear_coefficients((-2, -2), (-1, -2)))

print(linear_coefficients((1, -1), (-1, 1)))

print(linear_coefficients((2, 2), (3, 3)))
