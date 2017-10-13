def gender_conversion(matrix, column):
    """
    :param matrix: Matrix
    :param column: Int
    :return: Converted gender : Male = 1, Female = 0
    """
    for var_loop in range(len(matrix)):
        if matrix[var_loop, column] == 'male':
            matrix[var_loop, column] = 1
        else:
            matrix[var_loop, column] = 0
