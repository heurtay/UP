def section_sort(nums):
    n = len(nums)  # определяем длину списка
    zero = 0  # указатель на начало текущей секции (между нулями)

    for i in range(n):  # проходим по всем элементам списка
        if nums[i] == 0:  # если встречаем ноль
            nums[zero:i] = sorted(nums[zero:i])  # сортируем текущую секцию (от zero до i-1)
            zero = i + 1  # перемещаем указатель на начало следующей секции (после нуля)

    # после цикла проверяем, осталась ли неотсортированная секция в конце
    if zero < n:  # если zero не дошел до конца списка (последний элемент не ноль)
        nums[zero:] = sorted(nums[zero:])  # сортируем оставшуюся секцию


# Тестовые случаи:

nums = [2, 1, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)  # [1, 2, 0, 1, 2, 3, 0] (секции между нулями отсортированы)

nums = [1, 1, 1, 0, 5, 3, 4, 0, 2, 5, 3, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)  # [1, 1, 1, 0, 3, 4, 5, 0, 2, 3, 5, 0, 1, 2, 3, 0]

nums = [1, 1, 1, 0, 2, 2, 2, 0]
section_sort(nums)
print(nums)  # [1, 1, 1, 0, 2, 2, 2, 0] (уже отсортированные секции)

nums = [3, 2, 1, 0]
section_sort(nums)
print(nums)  # [1, 2, 3, 0] (первая секция отсортирована)

nums = [1, 0]
section_sort(nums)
print(nums)  # [1, 0] (одна секция из одного элемента)

nums = [5, 4, 3, 0, 2, 1, 0]
section_sort(nums)
print(nums)  # [3, 4, 5, 0, 1, 2, 0] (две секции отсортированы)