# 4. Write a python program to perform the Matrix Multiplication of two 3X3 Matrices.
# with numpy

import numpy as np

print("\nWith numpy - Matrix multiplication")
matrix1 = np.random.randint(1, 99, size=(3, 3))
matrix2 = np.random.randint(1, 99, size=(3, 3))
print("Generated matrix1: ")
print(matrix1)
print("Generated matrix2: ")
print(matrix2)
matrix_product = np.dot(matrix1, matrix2)
print("Product of the two matrices: ")
print(matrix_product)
