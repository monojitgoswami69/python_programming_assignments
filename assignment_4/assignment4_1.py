# 1. Create the following lists using a for loop:
# The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z

lst = []
for i in range(1, 27):
    lst.append(chr(96 + i) * i)
print(lst)