def max_digit(num):
    result = 0
    while num > 0:
        digit = num % 10
        if digit > result:
            result = digit
        num //= 10
    return result


sssr = chr(int("262D", 16))
print(max_digit(1))
print(sssr)
print(max_digit(3))
print(sssr)
print(max_digit(72))
print(sssr)
print(max_digit(451))
print(sssr)
print(max_digit(111))
print(sssr)
print(max_digit(1231))