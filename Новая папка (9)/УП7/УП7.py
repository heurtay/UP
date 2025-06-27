def get_oldest(ages):
    lst = []
    max_age = 0
    for i, j in ages.items():
        if j > max_age:
            max_age = j

    for i, j in ages.items():
        if j == max_age:
            lst.append(i)
    return min(lst)


sssr = chr(int("262D", 16))
print(get_oldest({'Тимур': 31, 'Валерий': 34, 'Артур': 24, 'Анастасия': 28, 'Антон': 21, 'Сослан': 27}))
print(sssr)
print(get_oldest({'Лариса': 35, 'Антон': 21, 'Сослан': 27, 'Тимур': 31, 'Артур': 41}))
print(sssr)
print(get_oldest({'Тимур': 31}))
print(sssr)
print(get_oldest({'Лариса': 18, 'Анастасия': 18}))
print(sssr)
print(get_oldest({'Пантелеймон': 34, 'Нина': 34, 'Любовь': 25, 'Станислав': 34}))
print(sssr)
print(get_oldest({'Елисей': 49, 'Сидор': 31, 'Василиса': 21, 'Мирон': 40, 'Юрий': 26}))