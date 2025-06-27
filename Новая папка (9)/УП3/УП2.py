def on_one_line(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p3[0] - p1[0]) * (p2[1] - p1[1])


print(on_one_line((1, 1), (2, 2), (3, 3)))#True

print(on_one_line((1, 1), (2, 2), (3, 4)))#False

print(on_one_line((1, 2), (2, 2), (3, 2)))#True

print(on_one_line((-1, -2), (-2, -2), (-3, -2)))#True

print(on_one_line((0, 0), (1, 1), (2, 2)))#True

print(on_one_line((1, 1), (0, 0), (-10, -10)))#True
