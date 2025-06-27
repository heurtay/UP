def binary_search(nums, target):
    if sorted(nums) == nums:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            elem = nums[middle]

            if elem == target:
                return middle
            if elem < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        elem = nums[middle]

        if elem == target:
            return middle
        if elem > target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


print(binary_search([10, 20, 30, 40, 50], 20))

print(binary_search([50, 40, 30, 20, 10], 20))

print(binary_search([10, 20, 30, 40, 50], 25))

print(binary_search([1], 1))

print(binary_search([-1, 0, 1], -1))

print(binary_search([1, 0, -1], -1))
