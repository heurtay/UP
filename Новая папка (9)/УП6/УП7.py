def find_peaks(nums):
    counter = 0
    for i in range(0, len(nums) - 1):
        if nums[i] < nums[i + 1] and i + 1 != len(nums) - 1:
            counter += 1
    return counter


sssr = chr(int("262D", 16))
print(find_peaks([16, 7, 18, 12, 13, 11, 19, 9, 10, 6]))    # 18, 13, 19 и 10
print(sssr)
print(find_peaks([1, -1, 1, -2, 2, -2, -3, 3, -3]))
print(sssr)
print(find_peaks([3, 1, 3]))
print(sssr)
print(find_peaks([3, 1, 0]))
print(sssr)
print(find_peaks([1, 3, 2]))
print(sssr)
print(find_peaks([1, 1, 1]))
