#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = [row[:] for row in matrix]
    for cell, row in enumerate(new_matrix):
        for cell2, col in enumerate(new_matrix):
            sq_matrix[cell][cell2] = row[cell2] ** 2
    return sq_matrix 
