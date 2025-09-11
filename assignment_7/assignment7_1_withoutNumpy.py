# 1. Write a python program to create a 3X3 Matrix randomly and calculate the sum of the diagonal elements.
# without numpy

import random

print("\nWithout numpy - Diagonal sum")
matrix = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix: ")
print(matrix)
diagonal_sum = sum(matrix[i][i] for i in range(3))
print(f"Sum of diagonal elements: {diagonal_sum}")
