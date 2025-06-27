def max_guests(n: int, m: int):
    return (n - 1) * m * 3


print(max_guests(5, 10))

print(max_guests(10, 10))

print(max_guests(2, 5))

print(max_guests(1, 5))

print(max_guests(2, 1))

print(max_guests(1, 1))