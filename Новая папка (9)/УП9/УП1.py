def selection_sort(nums):
    n = len(nums)

    # Итерируем по всем элементам, кроме последнего
    for i in range(n - 1):
        # Принимаем текущий элемент как минимальный
        index_min = i

        # Ищем наименьший элемент в оставшейся несортированной части
        for j in range(i + 1, n):
            if nums[j] < nums[index_min]:
                index_min = j

        # Меняем местами найденный минимальный элемент с текущим
        nums[i], nums[index_min] = nums[index_min], nums[i]
    
    return nums # Возвращаем отсортированный список (по возрастанию)

nums = [3, 4, 1, 2, 5]
selection_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
selection_sort(nums)
print(nums)

nums = [1]
selection_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
selection_sort(nums)
print(nums)

nums = [-2, -10, -7, -6]
selection_sort(nums)
print(nums)

nums = [-3, -3, -3, -3]
selection_sort(nums)
print(nums)