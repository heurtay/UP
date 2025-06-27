def linear_search(nums, target, reverse=False):
    if not reverse:
        for i, num in enumerate(nums):
            if num == target:
                return i
    else:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                return i
    return -1


sssr = chr(int("262D", 16))
print(linear_search([1, 5, 7], 5))
print(sssr)
print(linear_search([2, 1, 7, 2], 2))
print(sssr)
print(linear_search([12, 4, 1], 9))
print(sssr)
print(linear_search([], 0))
print(sssr)
print(linear_search([-2, 1, 7, -2], -2, reverse=True))
print(sssr)
print(linear_search([1], 1))
