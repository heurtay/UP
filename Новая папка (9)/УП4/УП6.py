def drop_one_and_five(n: int):
    counter = 0
    n1 = 0
    mult = 1
    while n > 0:
        n1 = n % 10
        n = n // 10

        if n1 != 1 and n1 != 5:
            counter += n1 * mult
            mult *= 10

    return counter


print(drop_one_and_five(527012))

print(drop_one_and_five(2468))

print(drop_one_and_five(0))

print(drop_one_and_five(1155))

print(drop_one_and_five(10))

print(drop_one_and_five(105))
