# 2. Write a python program to perform the addition of two 3X3 Matrices.
# with numpy

import numpy as np

print("\nWith numpy - Matrix addition")
matrix1 = np.random.randint(1, 99, size=(3, 3))
matrix2 = np.random.randint(1, 99, size=(3, 3))
print("Generated matrix1: ")
print(matrix1)
print("Generated matrix2: ")
print(matrix2)
matrix_sum = matrix1 + matrix2
print("Sum of matrices:")
print(matrix_sum)
