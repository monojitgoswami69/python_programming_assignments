# 1. Write a python program to create a 3X3 Matrix randomly and calculate the sum of the diagonal elements.
# with numpy

import numpy as np

print("\nWith numpy - Diagonal sum")
matrix = np.random.randint(1, 99, size=(3, 3))
print("Generated matrix: ")
print(matrix)
print(f"Sum of diagonal elements: {np.trace(matrix)}")