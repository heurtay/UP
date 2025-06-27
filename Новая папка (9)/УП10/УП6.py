from collections import Counter

def count_beautiful_pairs(nums):
    """
    Подсчитывает количество пар одинаковых чисел в списке.
    Каждые два одинаковых числа образуют одну пару.
    """
    count = Counter(nums)  # Создаём счётчик частот чисел
    answer = 0
    
    # Проходим по всем уникальным числам
    for num in count:
        # Добавляем количество пар для текущего числа (целочисленное деление на 2)
        answer += count[num] // 2
    
    return answer

# Альтернативный вариант с явным вычитанием пар:
# def count_beautiful_pairs(nums):
#     count = Counter(nums)
#     answer = 0
#     for num in count:
#         while count[num] >= 2:  # Пока есть хотя бы 2 одинаковых числа
#             answer += 1         # Увеличиваем счётчик пар
#             count[num] -= 2     # Удаляем использованную пару
#     return answer

# Тестовые случаи:

# [1,1], [4,4] → 2 пары (1 и 4)
print(count_beautiful_pairs([1, 4, 5, 4, 1, 1, 0]))  # Вывод: 2

# 7 четвёрок → 3 пары (4,4)
print(count_beautiful_pairs([4, 4, 4, 4, 4, 4, 4]))  # Вывод: 3

# Нет пар
print(count_beautiful_pairs([1, 2, 3, 4, 5, 6, 7]))  # Вывод: 0

# Одна пара нулей
print(count_beautiful_pairs([0, 0]))  # Вывод: 1

# Три единицы → одна пара
print(count_beautiful_pairs([1, 1, 1]))  # Вывод: 1

# Две пары: [0,0] и [9,9]
print(count_beautiful_pairs([0, 9, 9, 0]))  # Вывод: 2