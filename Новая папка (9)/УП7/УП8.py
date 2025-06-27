def min_product_of_two(nums: list):
    okok = sum(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i and nums[i] * nums[j] < okok:
                okok = nums[i] * nums[j]
    return okok


sssr = chr(int("262D", 16))
print(min_product_of_two([5, 2, 6, 1, 7]))
print(sssr)
print(min_product_of_two([1, 1, 1, 1, 1]))
print(sssr)
print(min_product_of_two([5, 4, 3, 2, 1]))
print(sssr)
print(min_product_of_two([1, 5, 4, 3, 2]))
print(sssr)
print(min_product_of_two([1, 2, 1, 3, 4]))
print(sssr)
print(min_product_of_two([3, 4, 5, 2, 2]))
