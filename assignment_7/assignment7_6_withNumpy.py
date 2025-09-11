# 6. Write a python program to perform addition, subtraction and multiplication of two complex matrices.
# with numpy

import numpy as np

print("\nWith numpy - Complex matrices operations")
matrix1 = np.random.randint(1, 9, size=(3, 3)) + 1j * np.random.randint(1, 9, size=(3, 3))
matrix2 = np.random.randint(1, 9, size=(3, 3)) + 1j * np.random.randint(1, 9, size=(3, 3))
print("Generated matrix1: ")
print(matrix1)
print("Generated matrix2: ")
print(matrix2)
mat_add = matrix1 + matrix2
mat_sub = matrix1 - matrix2
mat_mul = np.dot(matrix1, matrix2)
print("Added matrix: ")
print(mat_add)
print("Subtracted matrix: ")
print(mat_sub)
print("Multiplied matrix: ")
print(mat_mul)
