def is_value(values, target):
    left, right = 0, 1
    while values[right] > target:
        right *= 2

    while left <= right:
        middle = left + (right - left) // 2
        elem = values[middle]
        if elem == target:
            return True
        if elem > target:
            left = middle + 1
        else:
            right = middle - 1
    return False


values1 = list(range(4, -100000, -7))
values2 = [-(i ** 2 - 1) for i in range(1, -1000000, -1)]

print(is_value(values1, -17))
print(is_value(values1, 100))
print(is_value(values1, 4))
print(is_value(values2, -15))
print(is_value(values2, -159999))
print(is_value(values2, -640000))