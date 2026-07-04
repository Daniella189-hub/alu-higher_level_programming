#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ""
        for i in range(len(row)):
            if i == len(row) - 1:
                line += "{}".format(row[i])
            else:
                line += "{} ".format(row[i])
        print(line)
