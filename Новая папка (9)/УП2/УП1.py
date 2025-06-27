def get_quadrant(p):
    p1, p2 = p
    if p1 > 0 and p2 > 0:
        return 1

    elif p1 < 0 and p2 > 0:
        return 2

    elif p1 < 0 and p2 < 0:
        return 3

    elif p1 > 0 and p2 < 0:
        return 4

    else:
        return None

print(get_quadrant((3, 4)))
print(get_quadrant((-1, 2)))
print(get_quadrant((-3, -5)))
print(get_quadrant((1, -1)))
print(get_quadrant((5, 0)))
print(get_quadrant((0, 0)))
