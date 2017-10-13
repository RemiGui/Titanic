def embark_conversion(matrix, column):
    """
    :param matrix: Matrix
    :param column: Int
    :return: Converted embark data & giving 'S' to missing embark
    """
    for var_loop in range(len(matrix)):
        if matrix[var_loop, column] == 'C':
            matrix[var_loop, column] = 0
        elif matrix[var_loop, column] == 'Q':
            matrix[var_loop, column] = 2
        else:
            matrix[var_loop, column] = 1
