#!/usr/bin/python3
"""
Define a matrix whose element values are the results of division.
Args:
    matrix(int) and div(int):
""" 
def matrix_divided(matrix, div):
    if not all(isinstance(row, list) and all(isinstance(value, (int, float)) for value in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])  # Get the length of the first row

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        new_row = [round(value / div, 2) for value in row]
        result_matrix.append(new_row)

    return result_matrix
