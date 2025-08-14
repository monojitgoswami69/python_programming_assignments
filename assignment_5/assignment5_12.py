# 12. Write a program to find the median of a list of numbers.

lst = list(map(int, input("Enter the numbers: ").split()))
lst.sort()
if len(lst) % 2 == 1:
    median = lst[len(lst) // 2]
else:
    median = (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
print(f"The median is: {median}")