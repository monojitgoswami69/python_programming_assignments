# 9. Get the key corresponding to the minimum value from the dictionary above.
# data_set = {'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}

data_set = {'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}
min_key = min(data_set, key=data_set.get)
print(f"Key corresponding to the minimum value: {min_key}")