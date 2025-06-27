def matrix_search(matrix, target):
    for i in matrix:
        for j in i:
            if j == target:
                return True
    return False


data = [[2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]]

print(matrix_search(data, 5))

data = [[2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]]

print(matrix_search(data, 0))

data = [[1]]

print(matrix_search(data, 1))

data = [[-2, -1, 0],
        [1, 2, 3],
        [-5, -4, -3]]

print(matrix_search(data, 0))

data = [[-2, -1],
        [0, 1]]

print(matrix_search(data, -2))

data = [[-21, 2, 7, 8, 17],
        [-9, -2, -1, 4, 9],
        [-18, -11, -7, -6, 23],
        [-17, 0, 10, 18, 22],
        [-24, -15, -10, 11, 16]]

print(matrix_search(data, 16))