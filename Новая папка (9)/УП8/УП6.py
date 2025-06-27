from math import sqrt


def triangle_of_coins(n):
    return int(sqrt(1 + 8 + n - 1) // 2)


print(triangle_of_coins(3))

print(triangle_of_coins(5))

print(triangle_of_coins(6))

print(triangle_of_coins(9))

print(triangle_of_coins(1))

print(triangle_of_coins(2))
