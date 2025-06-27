def mystery(n):
    if n % 2 == 0:
        return n + 2
    return n + 1


print(mystery(1))
print(mystery(2))
print(mystery(3))
print(mystery(4))
print(mystery(5))
print(mystery(0))
print(mystery(10))
print(mystery(100))
print(mystery(1000))
print(mystery(999))