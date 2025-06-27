def  find_index(nums, target):
    left, right = 0, 1
    while nums[right] < target:
        right *= 2

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


nums1 = list(range(4, 100000, 3))
nums2 = [i**2 for i in range(1000000)]

print(find_index(nums1, 13))

print(find_index(nums1, 11))

print(find_index(nums1, 4))


print(find_index(nums2, 0))

print(find_index(nums2, 75345))

print(find_index(nums2, 9999800001))
