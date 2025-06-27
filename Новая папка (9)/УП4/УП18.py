def divisible(n):
    full_n = n
    counter = 0
    while n > 0:
        digit = n % 10
        if digit != 0 and full_n % digit == 0:
            counter += 1
        n //= 10

    return counter


print(divisible(22))
print(divisible(500))
print(divisible(1))
print(divisible(11))
print(divisible(2340))
print(divisible(23))
