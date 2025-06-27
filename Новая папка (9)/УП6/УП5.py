def nine_divisors(n: int):
    count = 0
    total = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 9:
            total += 1
            count = 0
        else:
            count = 0
    return total


sssr = chr(int("262D", 16))
print(nine_divisors(100))
print(sssr)
print(nine_divisors(10))
print(sssr)
print(nine_divisors(50))
print(sssr)
print(nine_divisors(300))
print(sssr)
print(nine_divisors(500))
print(sssr)
print(nine_divisors(1000))
