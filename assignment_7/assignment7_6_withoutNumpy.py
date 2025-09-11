# 6. Write a python program to perform addition, subtraction and multiplication of two complex matrices.
# without numpy

import random

print("\nWithout numpy - Complex matrices operations")
matrix1 = [[random.randint(1, 9) + 1j * random.randint(1, 9) for j in range(3)] for i in range(3)]
matrix2 = [[random.randint(1, 9) + 1j * random.randint(1, 9) for j in range(3)] for i in range(3)]

print("Generated matrix1:")
print(matrix1)
print("Generated matrix2:")
print(matrix2)

mat_add = [[matrix1[i][j] + matrix2[i][j] for j in range(3)] for i in range(3)]
mat_sub = [[matrix1[i][j] - matrix2[i][j] for j in range(3)] for i in range(3)]

mat_mul = [[0+0j for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            mat_mul[i][j] += matrix1[i][k] * matrix2[k][j]

print("Added matrix:")
print(mat_add)
print("Subtracted matrix:")
print(mat_sub)
print("Multiplied matrix:")
print(mat_mul)
