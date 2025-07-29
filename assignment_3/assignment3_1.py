#1. Reduce a string of lowercase characters in range ascii [‘a’..’z’] by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them. Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String.
#examples: Input- aaabccddd, output- abd; input- abba, output-empty string

def reduce_string(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop() 
        else:
            stack.append(char)  
    return ''.join(stack) if stack else "Empty String"
string = input("Enter a string: ")
print(f"\nInput- {string}")
print(f"Output- {reduce_string(string)}")
