# 11. Write a program that accepts a different number of arguments and returns the sum of only the positive values passed to it.

def sum_positive_values(*args):
    return sum(x for x in args if x > 0)
args = list(map(int, input("Enter the numbers: ").split()))
print(f"Sum of positive values: {sum_positive_values(*args)}")