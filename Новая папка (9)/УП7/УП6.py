def max_to_min(nums: list):
    max_nums = max(nums)
    min_nums = min(nums)
    for i in range(len(nums)):
        if nums[i] == max_nums:
            nums[i] = min_nums
    return nums


sssr = chr(int("262D", 16))
data = [1, 3, 3, 3, 4]
max_to_min(data)
print(data)
print(sssr)
data = [5, 4, 2, -2, 4, 2, 2, 5]
max_to_min(data)
print(data)
print(sssr)
data = [1]
max_to_min(data)
print(data)
print(sssr)
data = [1, 2, 1, 2, 1, 2]
max_to_min(data)
print(data)
print(sssr)
data = [1, 1, 1, -1, 1, 1, 0]
max_to_min(data)
print(data)
print(sssr)
data = [1, 1]
max_to_min(data)
print(data)