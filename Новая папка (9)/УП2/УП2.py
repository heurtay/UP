def is_point_in_rectangle(p, rect):
    x, y = p
    (r1, r2), (r3, r4) = rect
    if r1 < x < r3:
        if r2 < y < r4:
            return True
        else:
            return False
    else:
        return False




print(is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]))

print(is_point_in_rectangle((1, 0), [(1, 1), (3, 4)]))

print(is_point_in_rectangle((2, 1), [(1, 1), (3, 4)]))

print(is_point_in_rectangle((0, 0), [(-1, -1), (3, 3)]))

print(is_point_in_rectangle((3, 0), [(0, 0), (10, 1)]))

print(is_point_in_rectangle((-5, -6), [(-10, -7), (-4, -2)]))
