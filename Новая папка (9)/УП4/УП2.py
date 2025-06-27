def swap_digits(n: int):
        first = n // 100
        middle = (n // 10) % 10
        last = n % 10

        return last * 100 + middle * 10 + first


print(swap_digits(123))

print(swap_digits(500))