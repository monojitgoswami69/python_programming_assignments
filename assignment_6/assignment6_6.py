# 6. Write a function to print the prime numbers that can be expressed as the sum of some other prime numbers. Ex: 5=2+3, 17=2+3+5+7

from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def get_combinations(primes):
    temp = []
    for r in range(2, len(primes) + 1):
        for i in combinations(primes, r):
            if sum(i) in primes:
                temp.append([sum(i),i])
    temp = sorted(temp, key=lambda x: x[0])
    return temp

def print_combinations(combs):
    for s, c in combs:
        print(f"{s} = {' + '.join(map(str, c))}")

r = int(input("Enter the range: "))
primes = get_primes(r)
combs = get_combinations(primes)
print_combinations(combs)