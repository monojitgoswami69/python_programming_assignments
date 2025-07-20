#8. Write a program to check if a number is a magic number or not

def is_magic(n):
    while n >= 10:
        n = sum(int(x) for x in str(n))
    return n == 1
num = int(input("Enter a number: "))
if is_magic(num): print("Magic number")
else: print(f"Not Magic number")
