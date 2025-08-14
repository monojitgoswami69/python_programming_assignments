# 1. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_elements(lst):
    return list(set(lst))

lst = list(map(int, input("Enter the numbers: ").split()))
print("Sample List :", lst)
print("Unique List :", unique_elements(lst))