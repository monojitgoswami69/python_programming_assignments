# 4. Write a python program to perform the Matrix Multiplication of two 3X3 Matrices.
# without numpy

import random

print("\nWithout numpy - Matrix multiplication")
matrix1 = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix1: ")
print(matrix1)
matrix2 = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix2: ")
print(matrix2)
matrix3 = [[0 for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
print("Product of the two matrices: ")
print(matrix3)
