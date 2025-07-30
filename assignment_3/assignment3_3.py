# 3. Write a Python function to check whether a string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once. 
# For example : “The quick brown fox jumps over the lazy dog”

def is_pangram(s):
    s = set(i for i in s.lower() if i.isalpha())
    return len(s) == 26
sample = input("Enter a string: ")
if is_pangram(sample): print("The string is a pangram")
else: print("The string is not a pangram")
