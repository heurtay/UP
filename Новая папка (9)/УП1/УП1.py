def calculate(vars, values, exp):
    plp = {}
    for i in range(len(vars)):
        plp[vars[i]] = str(values[i])

    for i in plp:
        exp = exp.replace(i, plp[i])

    return eval(exp)


print(calculate('xyz', [1, 2, 3], 'x-y+z'))

print(calculate('dbcw', [3, 0, -2, -3], '-d-c-b+w'))

print(calculate('abcd', [0, 0, 0, 0], 'a+b+c+d'))

print(calculate('a', [4], 'a'))

print(calculate('v', [-2], 'v'))

print(calculate('ab', [2, 2], 'a+b'))
