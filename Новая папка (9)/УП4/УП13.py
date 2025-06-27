def even_odd(nums: list):
    counter = 0
    len_nums = len(nums)
    for i in nums:
        if i % 2 == 0:
            counter += 1

    if counter == 0 or counter == len_nums:
        return True
    return False


print(even_odd([1, 3, 5, 7]))
print(even_odd([-2, 4, -6, 8]))
print(even_odd([1, 3, 4]))
print(even_odd([0, 0, 0]))
print(even_odd([1]))
print(even_odd([10, 0]))
