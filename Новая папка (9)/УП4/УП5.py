def time_zone(h: int, a: int, b: int):
    arthur = (h - a + b) % 24
    return arthur


print(time_zone(12, 3, 7))

print(time_zone(12, -4, 4))

print(time_zone(12, 0, 0))

print(time_zone(0, 0, 0))

print(time_zone(6, -11, 12))

print(time_zone(23, 12, -11))
