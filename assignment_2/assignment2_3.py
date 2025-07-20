#3. Write a program to input N numbers and then print the second largest number

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers = list(set(numbers))  
numbers.sort()
if len(numbers) < 2: print("Second largest not available.")
else: print(f"Second largest number is {numbers[-2]}")