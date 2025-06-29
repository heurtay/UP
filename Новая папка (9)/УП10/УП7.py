from collections import Counter

def count_beautiful_pairs(nums):
    # Используем collections.Counter для подсчета частоты каждого числа в списке.
    # Например, если nums = [1, 4, 5, 4, 1, 1, 0], count будет Counter({1: 3, 4: 2, 5: 1, 0: 1}).
    count = Counter(nums)
    
    # Инициализируем 'answer' нулем. Эта переменная будет хранить общее количество найденных "красивых пар".
    answer = 0
    
    # Проходим по каждому уникальному числу (ключу) в объекте Counter 'count'.
    for num in count:
        # Для каждого числа вычисляем, сколько пар можно сформировать.
        # Поскольку пара требует два вхождения одного и того же числа, мы делим его общее количество на 2.
        # Целочисленное деление (//) автоматически обрабатывает случаи, когда количество вхождений нечетное,
        # эффективно игнорируя оставшееся одиночное число, которое не может образовать пару.
        # Например, если число встречается 3 раза, count[num] // 2 будет 3 // 2 = 1 (одна пара).
        # Если число встречается 2 раза, count[num] // 2 будет 2 // 2 = 1 (одна пара).
        answer += count[num] // 2
        
    # Возвращаем общее подсчитанное количество "красивых пар".
    return answer

# Тестовые случаи:
print(count_beautiful_pairs([1, 4, 5, 4, 1, 1, 0])) # Ожидаемый результат: 1 (для четверок) + 1 (для единиц) = 2
print(count_beautiful_pairs([4, 4, 4, 4, 4, 4, 4])) # Ожидаемый результат: 7 // 2 = 3
print(count_beautiful_pairs([1, 2, 3, 4, 5, 6, 7])) # Ожидаемый результат: 0
print(count_beautiful_pairs([0, 0])) # Ожидаемый результат: 1
print(count_beautiful_pairs([1, 1, 1])) # Ожидаемый результат: 1
print(count_beautiful_pairs([0, 9, 9, 0])) # Ожидаемый результат: 1 (для нулей) + 1 (для девяток) = 2