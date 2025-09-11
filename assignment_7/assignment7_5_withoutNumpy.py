# 5. Write a python program to find row wise maximum and column wise minimum element(s).
# without numpy

import random

print("\nWithout numpy - Row-wise max & Column-wise min")
matrix = [[random.randint(1, 99) for j in range(3)] for i in range(3)]
print("Generated matrix: ")
print(matrix)
row_max = [max(i) for i in matrix]
col_min = [min(matrix[i][j] for i in range(3)) for j in range(3)]
print(f"Row wise maximum: {row_max}")
print(f"Column wise minimum: {col_min}")
