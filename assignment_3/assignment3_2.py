# 2. Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.

def count_case(s):
    upper_count = lower_count = 0
    for char in s:
        if char.isupper(): upper_count += 1
        elif char.islower(): lower_count += 1
    return upper_count, lower_count
sample = input("Enter a string: ")
upper, lower = count_case(sample)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
    