#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = matrix.copy()
    matrix_len = len(matrix)
    for index in range(matrix_len):
        square_matrix[index] = list(map(lambda x: x**2, matrix[index]))

    return square_matrix
