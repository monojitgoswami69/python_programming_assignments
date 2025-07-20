#2. Write a short program to check whether the square root of a number is prime or not

import math
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
num = int(input("Enter a number: "))
num = math.isqrt(num)
if is_prime(num): print("Square root is prime")
else: print("Square root is not prime")