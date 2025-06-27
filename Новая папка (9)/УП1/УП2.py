def is_function(pairs):
    fignya = []
    for i in pairs:
        fignya.append(i[0])
    if len(fignya) == len(set(fignya)):
        return True
    else:
        return False


print(is_function([(1, 3), (2, 5), (3, 7)]))

print(is_function([(1, 3), (2, 5), (1, 7)]))

print(is_function([(1, 3)]))

print(is_function([(5, 5)]))

print(is_function([(1, 1), (2, 2)]))

print(is_function([(1, 1), (1, 2)]))
