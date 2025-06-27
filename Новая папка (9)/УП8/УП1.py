def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        elem = data[middle]
        if elem == target:
            return middle
        if elem < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


print(binary_search([10, 20, 30, 40, 50], 40))

print(binary_search([10, 20, 30, 40, 50], 60))

print(binary_search([1, 2, 3, 4, 5], 1))

print(binary_search([1, 2, 3, 4], 4))

print(binary_search([1], 1))

print(binary_search([-1, 0, 1], -1))