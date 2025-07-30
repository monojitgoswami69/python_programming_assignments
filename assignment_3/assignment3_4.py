# 4. Write a program to check whether a user input string is palindrome or not

sample = input("Enter a string: ")
print("Palindrome" if sample == sample[::-1] else "Not a palindrome")
