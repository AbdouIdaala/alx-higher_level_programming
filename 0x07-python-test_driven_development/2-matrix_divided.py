#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list): list of lists of integers or floats
        div (int, float): divisor

    Raises:
        TypeError: div must be a number
        ZeroDivisionError: div must not equal to 0
        TypeError: the length of all lists in the matrix must be equal
        TypeError: the matrix must be a list of lists of integers or floats

    Returns:
        list: new matrix with all elements divided by 2
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, type([])):
        for element in matrix:
            if isinstance(element, type([])):
                length = len(matrix[0])
                if len(element) != length:
                    raise TypeError(
                        "Each row of the matrix must have the same size")
                for n in element:
                    if not isinstance(n, (int, float)):
                        raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")
            else:
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                        of integers/floats")
    else:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    copy_matrix = [[float("{:.2f}".format((n / div)))
                    for n in row] for row in matrix]
    return copy_matrix
