#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(x):
        return x ** 2
    
    square1 = [list(map(square, n)) for n in matrix]
    return square1
