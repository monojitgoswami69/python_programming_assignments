# 6.Merge following two Python dictionaries into one dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
merged_dict = {**dict1, **dict2}
print(f"Merged Dictionary: {merged_dict}")