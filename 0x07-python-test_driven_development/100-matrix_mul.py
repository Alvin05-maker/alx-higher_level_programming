#!/usr/bin/python3
"""
Define a function for multiplication of matrices
Args: 
    m_a and m_b.
"""
def matrix_mul(m_a, m_b):
    """
    Representation of matrix multiplication function.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if elements in m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b have a valid shape for multiplication
    columns_m_a = len(m_a[0])
    rows_m_b = len(m_b)
    if columns_m_a != rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
