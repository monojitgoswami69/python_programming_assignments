# 5. Write a program to display the maximum and minimum values from the specified range of indices of the list.

lst = list(map(int, input("Enter the numbers: ").split()))
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
print(f"Given range: {lst[start:end+1]}")
print(f"Maximum value: {max(lst[start:end+1])}")
print(f"Minimum value: {min(lst[start:end+1])}")