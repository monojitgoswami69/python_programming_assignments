# 5. In the Byteland country, a string S is said to super ASCII string if and only if the count of each character in the string is equal to its ASCII value. In the Byteland country ASCII code of 'a' is 1, 'b' is 2, ..., 'z' is 26. The task is to find out whether the given string is a super ASCII string or not. If true, then print "Yes" otherwise print "No".

def is_super_ascii(s):
    char = {}
    for i in range (ord('a'), ord('z') + 1):
        char[chr(i)] = i - ord('a') + 1
    for c in s:
        if c.isalpha():
            if s.count(c) != char[c]:
                return False
    return True

string = input("Enter a string: ")
if is_super_ascii(string):
    print("Super ASCII string")
else:
    print("Not a Super ASCII string")
