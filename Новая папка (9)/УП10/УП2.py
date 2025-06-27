def binary_insertion_sort(nums):
    n = len(nums)  # определяем длину списка

    # начинаем с первого элемента (индекс 1), так как элемент с индексом 0 считается отсортированным
    for i in range(1, n):
        index = nums[i]  # текущий элемент, который нужно вставить в отсортированную часть
        left, right = 0, i - 1  # границы бинарного поиска (отсортированная часть)

        # бинарный поиск места для вставки элемента
        while left <= right:
            mid = (left + right) // 2  # находим середину текущего диапазона
            if nums[mid] < index:  # если середина меньше вставляемого элемента,
                left = mid + 1     # значит, искомое место справа от mid
            else:                  # иначе — слева от mid
                right = mid - 1

        # сдвигаем элементы вправо, чтобы освободить место для вставки
        for j in range(i, left, -1):  # идём от текущего элемента (i) до места вставки (left)
            nums[j] = nums[j - 1]     # сдвигаем элементы вправо

        nums[left] = index  # вставляем элемент на найденное место


# тестовые случаи
nums = [3, 4, 1, 2, 5]
binary_insertion_sort(nums)
print(nums)  # [1, 2, 3, 4, 5] (отсортировано по возрастанию)

nums = [3, 2, 2, 1, 3, 3]
binary_insertion_sort(nums)
print(nums)  # [1, 2, 2, 3, 3, 3]

nums = [1]
binary_insertion_sort(nums)
print(nums)  # [1] (массив из одного элемента уже отсортирован)

nums = [5, 4, 3, 2, 1]
binary_insertion_sort(nums)
print(nums)  # [1, 2, 3, 4, 5] (отсортировано по возрастанию)

nums = [-2, -10, -7, -6]
binary_insertion_sort(nums)
print(nums)  # [-10, -7, -6, -2] (отсортировано по возрастанию)

nums = [-3, -3, -3, -3]
binary_insertion_sort(nums)
print(nums)  # [-3, -3, -3, -3] (все элементы одинаковы)
