def avg_values(nums):
    lst_avg = []
    lst_preavg = []
    for i in range(len(nums)):
        lst_preavg.append(nums[i])
        lst_avg.append(sum(lst_preavg) / len(lst_preavg))

    return lst_avg


print(avg_values([10, 20, 30, 40, 50]))
print(avg_values([1, 1, 1, 1, 1]))
print(avg_values([-2, -3, 5, 5]))
print(avg_values([]))
print(avg_values([0, 0, 0, 0]))
print(avg_values([3]))
