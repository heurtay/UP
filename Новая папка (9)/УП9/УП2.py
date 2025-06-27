def sum_of_seven_smallest(nums):
    n = len(nums)

    # Внешний цикл для проходов по массиву
    for i in range(n - 1):
        # Предполагаем, что текущий элемент - минимальный
        index_min = i

        # Внутренний цикл для поиска наименьшего элемента в оставшейся части
        for j in range(i + 1, n):
            # Если найден элемент меньше текущего минимума, обновляем index_min
            if nums[j] < nums[index_min]:
                index_min = j

        # Меняем местами текущий элемент с найденным минимальным
        nums[i], nums[index_min] = nums[index_min], nums[i]
    
    # Инициализируем счетчик для суммы
    counter = 0
    # Суммируем первые 7 (наименьших) элементов после сортировки
    for i in range(7):
        counter += nums[i]
    return counter

# Тестовые случаи
print(sum_of_seven_smallest([2, 7, 3, 6, 10, 4, 1, 9, 5, 8]))
print(sum_of_seven_smallest([2, 2, 4, 1, 3, 3, 5, 4, 4]))
print(sum_of_seven_smallest([1, 1, 1, 1, 1, 1, 1, 1]))
print(sum_of_seven_smallest([-1, 1, -1, 1, -1, 1, -1, 1]))
print(sum_of_seven_smallest([-50, 15, 15, 20, 10, 15, 3, 2, 5]))
print(sum_of_seven_smallest([-7, -2, -2, -8, -1, -4, -10]))