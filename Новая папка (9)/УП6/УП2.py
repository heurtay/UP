def equal(nums: list) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] == i:
            return i
    return -1


sssr = chr(int("262D", 16))
print(equal([10, 7, 2]))
print(sssr)
print(equal([2, 1, 4, 3]))
print(sssr)
print(equal([2, 9, 4, 8]))
print(sssr)
print(equal([0]))
print(sssr)
print(equal([0, 1, 2, 3]))
print(sssr)
print(equal([]))
