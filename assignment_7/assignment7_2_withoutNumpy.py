# 2. Write a python program to perform the addition of two 3X3 Matrices.
# without numpy

import random

print("\nWithout numpy - Matrix addition")
matrix1 = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix1: ")
print(matrix1)
matrix2 = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix2: ")
print(matrix2)
matrix_sum = [[matrix1[i][j] + matrix2[i][j] for j in range(3)] for i in range(3)]
print("Sum of matrices:")
print(matrix_sum)
