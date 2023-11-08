def square_matrix_simple(matrix=[]):
    sq_matrix = [row[:] for row in matrix]
    
    for row_idx, row in enumerate(sq_matrix):
        for col_idx, cell in enumerate(row):
            sq_matrix[row_idx][col_idx] = cell ** 2

    return sq_matrix
