# 3. Write programs as per following specifications: ''Print the length of the longest string in the list of strings str_list. Precondition : the list will contain at least one element.

lst = list(map(str, input("Enter the strings: ").split()))
if not lst:
    print("List is empty")
else:
    max_length = max(len(s) for s in lst)
    print("Length of the longest string:", max_length)