def max_of_two(a, b):
    if a < b:
        return b
    return a


def max_of_four(a, b, c, d):
    max_of_two(a, b)
    max_of_two(c, d)
    return max_of_two(max_of_two(a, b), max_of_two(c, d))


sssr = chr(int("262D", 16))
print(max_of_four(4, 9, 10, 5))
print(sssr)
print(max_of_four(0, -1, -1, 0))
print(sssr)
print(max_of_four(-3, -5, -1, -2))
print(sssr)
print(max_of_four(1, -2, -1, 2))
print(sssr)
print(max_of_four(10, 1, 1, 1))