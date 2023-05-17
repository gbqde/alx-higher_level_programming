#!/usr/bin/python3
# Author: Gbade Moses (@gbqde)

def square_matrix_map(matrix=[]):
    return list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
