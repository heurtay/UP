def snake(n: int):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print("*" * n)
        elif i % 4 == 0:
            print("*")
        else:
            print(" " * (n - 1) + "*")


snake(1)
print( )

snake(3)
print()

snake(4)
print()

snake(5)
