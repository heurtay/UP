def search_insert_position(nums, target):
    if target in nums:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        return -1
    else:
        n = len(nums)
        for i in range(n):
            if nums[i] != target:
                nums.append(target)
                sorted_nums = sorted(nums)
            return sorted_nums.index(target)


sssr = chr(int("262D", 16))
print(search_insert_position([1, 2, 3, 4, 5], 5))
print(sssr)
print(search_insert_position([1, 2, 3, 4, 5], 6))
print(sssr)
print(search_insert_position([1, 2, 4, 5], 3))
print(sssr)
print(search_insert_position([2, 3, 4, 5, 6], 1))
print(sssr)
print(search_insert_position([1], 2))
print(sssr)
print(search_insert_position([1], 1))
