def count_numbers(n: int, k: int):
    count = 0
    for i in range(1, n + 1):
        if i - sum([int(j) for j in str(i)]) >= k:
            count += 1
    return count


sssr = chr(int("262D", 16))
print(count_numbers(13, 2))
print(sssr)
print(count_numbers(10, 5))
print(sssr)
print(count_numbers(1, 0))
print(sssr)
print(count_numbers(10, 0))
print(sssr)
print(count_numbers(10, 1))
print(sssr)
print(count_numbers(10, 15))
