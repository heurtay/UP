def min_digit_sum(a, b):
    digit_sum = lambda n: sum([int(d) for d in str(n)])
    s = [digit_sum(x) for x in range(a, b + 1)]
    return s.count(min(s))


print(min_digit_sum(1, 50))
print(min_digit_sum(1, 100))
print(min_digit_sum(50, 200))
print(min_digit_sum(1, 1))
print(min_digit_sum(1, 1000))
print(min_digit_sum(456, 678))
