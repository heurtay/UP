def mystery(n: int):
    number = sum([x for x in range(1, n + 1)])
    return number


print(mystery(4))
print(mystery(1))
print(mystery(500))
