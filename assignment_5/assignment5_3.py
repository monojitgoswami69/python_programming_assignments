# 3. Copy element 44 and 55 from the following tuple into a new tuple tuple1 = (11, 22, 33, 44, 55, 66)
tuple1 = (11, 22, 33, 44, 55, 66)
new_tuple = tuple(i for i in tuple1 if i in (44, 55))
print(f"New Tuple: {new_tuple}")