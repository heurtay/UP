def find_triple(nums):
    s = max(nums)
    lst = nums.copy()
    lst.remove(s)
    a = s - lst[2]
    b = s - lst[1]
    c = s - lst[0]
    return sorted([a, b, c])


print(find_triple([8, 5, 7, 4]))

print(find_triple([2, 2, 3, 2]))

print(find_triple([5, 3, 6, 4]))

print(find_triple([600000000, 600000000, 600000000, 900000000]))

print(find_triple([3, 5, 3, 4]))
