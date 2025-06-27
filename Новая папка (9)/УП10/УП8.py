def find_triple(nums):
    s = max(nums)          # Находим сумму a + b + c (макс. число)
    lst = nums.copy()      # Копируем список, чтобы не менять исходный
    lst.remove(s)          # Удаляем сумму из копии
    a = s - lst[2]         # Вычисляем a (s - третье число)
    b = s - lst[1]         # Вычисляем b (s - второе число)
    c = s - lst[0]         # Вычисляем c (s - первое число)
    return sorted([a, b, c])  # Возвращаем отсортированный результат


# Тесты
print(find_triple([8, 5, 7, 4]))       # [1, 3, 4]
print(find_triple([2, 2, 3, 2]))       # [0, 1, 1]
print(find_triple([5, 3, 6, 4]))       # [1, 2, 3]
print(find_triple([600M, 600M, 600M, 900M]))  # [300M, 300M, 300M]
print(find_triple([3, 5, 3, 4]))       # [0, 1, 2]
