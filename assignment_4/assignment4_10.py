# 10. Write a program to find the arithmetic mean, variance and standard deviation of any values in a list.

lst = list(map(int, input("Enter the numbers: ").split()))
n = len(lst)
mean = sum(lst) / n
lst = [(x - mean) ** 2 for x in lst]
var = sum(lst) / n
sd = var ** 0.5
print(f"Mean: {mean}")
print(f"Variance: {var}")
print(f"Standard Deviation: {sd}")
