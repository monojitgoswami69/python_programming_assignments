# 4. Modify the first item (22) of a list inside a following tuple to 222 tuple1 = (11, [22, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(f"Modified Tuple: {tuple1}")