def max_sum_of_k_elements(nums, k):
    # Сортируем список чисел по возрастанию.
    # Например, [4, 2, 3, 1] станет [1, 2, 3, 4].
    sorted_nums = sorted(nums)
    
    # Берем последние 'k' элементов из отсортированного списка.
    # Это будут 'k' наибольших чисел.
    # Например, если k=2 для [1, 2, 3, 4], мы возьмем [3, 4].
    k_largest_elements = sorted_nums[-k:]
    
    # Суммируем эти 'k' наибольших элементов и возвращаем результат.
    # Для примера выше, sum([3, 4]) будет 7.
    return sum(k_largest_elements)

# Тестовые случаи
print(max_sum_of_k_elements([4, 2, 3, 1], 2))      # Ожидается 7 (3 + 4)
print(max_sum_of_k_elements([-2, 4, 0, -3], 2))   # Ожидается 4 (0 + 4)
print(max_sum_of_k_elements([1], 1))              # Ожидается 1
print(max_sum_of_k_elements([-1, 1, -1, 1], 4))   # Ожидается 0 (-1 + 1 + -1 + 1)
print(max_sum_of_k_elements([-1, -2, -3], 3))    # Ожидается -6 (-1 + -2 + -3)
print(max_sum_of_k_elements([0, 2, 4, 6], 1))     # Ожидается 6