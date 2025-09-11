# 5. Write a python program to find row wise maximum and column wise minimum element(s).
# with numpy

import numpy as np

print("\nWith numpy - Row-wise max & Column-wise min")
matrix = np.random.randint(1, 99, size=(3, 3))
print("Generated matrix: ")
print(matrix)
row_max = np.max(matrix, axis=1)
col_min = np.min(matrix, axis=0)
print(f"Row wise maximum: {row_max}")
print(f"Column wise minimum: {col_min}")
