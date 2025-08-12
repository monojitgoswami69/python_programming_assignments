# 6. Write a program to move all duplicate values in a list to the end of the list

lst = list(map(int, input("Enter the numbers: ").split()))
unique = []
duplicate = []
for i in lst:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
lst = unique + duplicate
print(f"List after moving duplicates to the end: {lst}")