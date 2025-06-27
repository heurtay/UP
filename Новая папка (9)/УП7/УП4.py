def min_max_diff(nums):
    # return max(nums) - min(nums)

    max_nums = 0
    min_nums = sum(nums)
    for i in nums:
        if i > max_nums:
            max_nums = i
        if i < min_nums:
            min_nums = i
    return max_nums - min_nums


sssr = chr(int("262D", 16))
print(min_max_diff([4, 5, 3, 2, 1]))
print(sssr)
print(min_max_diff([5, 5, 5, 5, 5]))
print(sssr)
print(min_max_diff([1, 2]))
print(sssr)
print(min_max_diff([10, 10]))
print(sssr)
print(min_max_diff([1]))
print(sssr)
print(min_max_diff([-10, -5, 0, 5, 10]))