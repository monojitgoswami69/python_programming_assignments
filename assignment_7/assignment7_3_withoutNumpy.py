# 3. Write a python program to perform the elements-wise multiplication of two 3X3 Matrices.
# without numpy

import random

print("\nWithout numpy - Element-wise product")
matrix1 = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix1: ")
print(matrix1)
matrix2 = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix2: ")
print(matrix2)
matrix_product = [[matrix1[i][j] * matrix2[i][j] for j in range(3)] for i in range(3)]
print("Product of matrices (element wise):")
print(matrix_product)
