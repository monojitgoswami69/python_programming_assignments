#7. Write a program to print the following pattern using numbers (full pyramid/diamond)

n = int(input("Enter the range "))
# Calculate field width based on the largest number
field_width = len(str(n))

for i in range(1, n + 1):
    print(" " * (n - i) * field_width , end="")
    for j in range(1, i + 1):
        print(f"{j:>{field_width}}", end=" "*field_width)
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i) * field_width, end="")
    for j in range(1, i + 1):
        print(f"{j:>{field_width}}", end=" "*field_width)
    print()
