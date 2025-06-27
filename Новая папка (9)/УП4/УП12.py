def sum_of_squares(n: int):
    return sum([x ** 2 for x in range(1, n + 1)])


print(sum_of_squares(1))
print(sum_of_squares(2))
print(sum_of_squares(3))
print(sum_of_squares(5))
