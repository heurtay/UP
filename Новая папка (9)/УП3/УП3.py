def equation_of_line(values):
    b = values[0]
    k = values[1] - values[0]

    if len(set(values)) == 1:
        return f"y = {values[0]}"
    elif values[1] - values[0] == 0:
        return None
    elif k != 0 and b != 0:
        return f"y = {k}x + {b}"
    elif b == 0 and k == 1:
        return f"y = x"
    elif b == 0 and k < 0:
        if k == -1:
            return f"y = -x"
        return f"y = {k}x"






print(equation_of_line([0, 1, 2, 3, 4])) # y = x

print(equation_of_line([0, -1, -2, -3, -4])) # y = -x

print(equation_of_line([0, -2, -4, -6, -8])) # y = -2x

print(equation_of_line([1, 3, 5, 7, 9])) # y = 2x + 1

print(equation_of_line([6, 6, 6, 6, 6])) # y = 6

print(equation_of_line([1, 1, 2, 2, 2])) # None