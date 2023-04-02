#!/usr/bin/python3

"""A module to divide a matrix

Args:

Attributes:
"""


def matrix_divided(matrix, div):
    """A funtion that divides all elements
    of a matrix

    Args:
        matrix (list): A list of lists of integers or floats
        div (int or float): The divisor of the matrix

    Returns:
        list: the matrix divided by the divisor

    Raises:
        TypeError: If matrix is of the wrong type or not uniform,
            or div is not an in or float
        ZeroDivisionError: if div is zero
    """

    mat_list = isinstance(matrix, list)
    # Check that sub elements of matrix are lists
    try:
        sub_lists = False not in [isinstance(sub, list) for sub in matrix]

        # Check that all sub sub elements are integers/floats
        int_float = [isinstance(e, int) or isinstance(e, float)
                     for sub in matrix for e in sub]
        int_float = False not in int_float
    except Exception:
        sub_lists = False
        int_float = False

    if not (mat_list and sub_lists and int_float):
        raise TypeError("matrix must be a matrix (list of lists)\
             of integers/floats")

    n = len(matrix[0])
    for sub in matrix:
        if len(sub) != n:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int or float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            matrix[i][j] /= div
            matrix[i][j] = round(matrix[i][j], 2)
            j += 1
        i += 1

    return matrix
