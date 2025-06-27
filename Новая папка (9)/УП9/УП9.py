def k_swaps_to_sort(n, k):
    """
    Генерирует перестановку чисел от 1 до n, которая требует ровно k обменов
    при сортировке пузырьком.
    """
    result = []  # Список, в который будем добавлять числа
    inv_remaining = k  # Количество "инверсий" (обменов), которые нужно создать

    # Итерируем от 1 до n, добавляя каждое число в список
    for i in range(1, n + 1):
        current_length = len(result)  # Текущая длина списка result
        
        # Вычисляем x: сколько элементов i "пройдет" мимо, создавая x инверсий.
        # Это не превысит inv_remaining и текущую длину списка.
        x = min(inv_remaining, current_length)
        
        # Вычисляем позицию для вставки: current_length - x означает
        # вставку на x позиций от конца списка.
        pos = current_length - x
        
        result.insert(pos, i)  # Вставляем число i на вычисленную позицию
        inv_remaining -= x  # Уменьшаем количество оставшихся инверсий
        
    return result


def number_of_swaps(nums):
    """
    Вычисляет количество обменов, необходимых для сортировки списка nums
    по возрастанию с помощью пузырьковой сортировки.
    """
    n = len(nums)
    counter = 0  # Счетчик обменов

    # Внешний цикл: каждый проход "всплывает" наибольший элемент в конец
    for i in range(n - 1):
        swapped = False  # Флаг для отслеживания обменов в текущем проходе

        # Внутренний цикл: сравниваем соседние элементы и меняем их местами, если они не по порядку
        # n - i - 1: диапазон уменьшается, так как последние i элементов уже отсортированы
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                counter += 1  # Увеличиваем счетчик обменов
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Выполняем обмен
                swapped = True  # Отмечаем, что обмен произошел

        # Оптимизация: если в проходе не было обменов, список уже отсортирован
        if not swapped:
            break
            
    return counter  # Возвращаем общее количество обменов


# Примеры использования:
print(number_of_swaps(k_swaps_to_sort(5, 3)))
print(number_of_swaps(k_swaps_to_sort(1, 0)))
print(number_of_swaps(k_swaps_to_sort(5, 1)))
print(number_of_swaps(k_swaps_to_sort(5, 10)))
print(number_of_swaps(k_swaps_to_sort(7, 4)))
print(number_of_swaps(k_swaps_to_sort(10, 45)))