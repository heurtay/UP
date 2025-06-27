def binary_search(nums, target, left=0, right=0):
    left, right = 0, len(nums) - 1

    while right >= left:
        middle = (left + right) // 2
        elem = nums[middle]

        if elem == target:
            return middle
        if elem < target:
            right = middle - 1
        else:
            left = middle + 1
    return -1


print(binary_search([50, 40, 30, 20, 10], 30))

print(binary_search([50, 40, 30, 20, 10], 0))

print(binary_search([5, 4, 3, 2, 1], 5))

print(binary_search([5], 5))

print(binary_search([1, 0, -1], -1))

print(binary_search([5, 4, 3, 2, 1], 1))