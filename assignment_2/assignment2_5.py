#5. Calculate the factorial of a number both recursively and non-recursively

# Recursive
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)
# Non-recursive
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1): result *= i
    return result
num = int(input("Enter a number: "))
print(f"Recursive: {factorial_recursive(num)}")
print(f"Non-recursive: {factorial_iterative(num)}")
