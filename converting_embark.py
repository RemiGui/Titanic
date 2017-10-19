def embark_conversion(matrix, column):
    """
    :param matrix: Matrix
    :param column: Int
    :return: Converted embark data & giving 'S' to missing embark
    """
    for line in range(len(matrix)):
        if matrix[line, column] == 'C':
            matrix[line, column] = 0
        elif matrix[line, column] == 'Q':
            matrix[line, column] = 2
        else:
            matrix[line, column] = 1
