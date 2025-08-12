# 8. Write a program to reverse a list without using another list or in-built function.
lst = list(map(int, input("Enter the numbers: ").split()))
n = len(lst)
for i in range(n // 2):
    lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
print(f"Reversed list: {lst}")
