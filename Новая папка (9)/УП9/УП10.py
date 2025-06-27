def cocktail_sort(nums):
    n = len(nums)
    # Определяем диапазон индексов для итерации (до предпоследнего элемента)
    # left_bound и right_bound будут использоваться для сужения диапазона сортировки
    left_bound = 0
    right_bound = n - 1
    
    # Сортировка продолжается до тех пор, пока происходят обмены
    while True:
        swapped = False # Флаг для отслеживания обменов в текущем проходе

        # --- Проход слева направо (как в пузырьковой сортировке) ---
        # Итерируем от левой границы до правой (почти до конца)
        for i in range(left_bound, right_bound):
            # Если текущий элемент больше следующего, меняем их местами
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True # Отмечаем, что обмен произошел
        
        # Если в этом проходе не было обменов, список отсортирован
        if not swapped:
            return nums
        
        # Если были обмены, сдвигаем правую границу влево, 
        # так как самый большой элемент находится на своем месте
        right_bound -= 1
        swapped = False # Сбрасываем флаг для следующего прохода

        # --- Проход справа налево ---
        # Итерируем от правой границы вниз до левой границы
        for i in range(right_bound, left_bound, -1):
            # Если текущий элемент меньше предыдущего, меняем их местами
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                swapped = True # Отмечаем, что обмен произошел
        
        # Если в этом проходе не было обменов, список отсортирован
        if not swapped:
            return nums
        
        # Если были обмены, сдвигаем левую границу вправо,
        # так как самый маленький элемент находится на своем месте
        left_bound += 1


# Тестовые примеры
data = [8, 9, 6, 5, 7, 4, 1, 2, 3]
cocktail_sort(data)
print(data)

data = [5, 4, 3, -2, 1]
cocktail_sort(data)
print(data)

data = [3]
cocktail_sort(data)
print(data)

data = [1, 2, 3, 4, 5]
cocktail_sort(data)
print(data)

data = [2, 1]
cocktail_sort(data)
print(data)

data = [1, 1, 1, 1, 1]
cocktail_sort(data)
print(data)

data = [8, 9, 6]
cocktail_sort(data)
print(data)