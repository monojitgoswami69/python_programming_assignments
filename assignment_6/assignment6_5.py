# 5. Write a function to implement Binary search.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = list(map(int, input("Enter the numbers: ").split()))

if not numbers:
    print("Empty list provided!")
    exit()

if numbers != sorted(numbers):
    print("Array is not sorted. Sorting it first...")
    numbers.sort()
    print(f"Sorted array: {numbers}")

target = int(input("Enter the number to search: "))
result = binary_search(numbers, target)

if result != -1: 
    print(f"\nElement {target} found at index {result}")
else: 
    print(f"\nElement {target} not found in the array")
