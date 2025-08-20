# 3. Write a single function to return maximum and minimum value from a list along with the indices.

def calcMaxMin(numbers):
    max_value, max_index = max((num, i) for i, num in enumerate(numbers))
    min_value, min_index = min((num, i) for i, num in enumerate(numbers))
    return (max_value, max_index), (min_value, min_index)

numbers = list(map(float, input("Enter the numbers: ").split()))
if not numbers:
    print("Empty list provided!")
    exit(1)
else:
    (max_val, max_idx), (min_val, min_idx) = calcMaxMin(numbers)
    print(f"\nList: {numbers}")
    print(f"Maximum value: {max_val} at index {max_idx}")
    print(f"Minimum value: {min_val} at index {min_idx}")
