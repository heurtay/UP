def bubble_sort(nums):                                         # data – список значений
    n = len(nums)

    for i in range(n - 1):
        swapped = False                                        # определяем переменную для отслеживания обменов

        for j in range(n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True                                 # отмечаем, если в ходе прохода совершается обмен

        if not swapped:                                        # если за весь проход не было ни одного обмена,
            break


nums = [3, 4, 1, 2, 5]
bubble_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
bubble_sort(nums)
print(nums)

nums = [1]
bubble_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
bubble_sort(nums)
print(nums)

nums = [-2, -10, -7, -6]
bubble_sort(nums)
print(nums)

nums = [-3, -3, -3, -3]
bubble_sort(nums)
print(nums)
