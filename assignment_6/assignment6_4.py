#4. Write a function to implement Bubble sort.

def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr

numbers = list(map(int, input("Enter the numbers: ").split()))
if not numbers:
    print("Empty list provided!")
    exit()
print(f"\nOriginal array: {numbers}")
sorted_numbers = bubble_sort(numbers)
print(f"Sorted array: {sorted_numbers}")
    