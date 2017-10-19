def gender_conversion(matrix, column):
    """
    :param matrix: Matrix
    :param column: Int
    :return: Converted gender : Male = 1, Female = 0
    """
    for line in range(len(matrix)):
        if matrix[line, column] == 'male':
            matrix[line, column] = 1
        else:
            matrix[line, column] = 0
