# 2. Write a python program to show the permutation and combination of an user input list

from itertools import permutations, combinations

lst = list(map(int, input("Enter the numbers: ").split()))

print("Permutations:")
for i in range(2, len(lst) + 1):
    for p in permutations(lst, i):
        print(p)        

print("Combinations:")
for i in range(2, len(lst) + 1):
    for c in combinations(lst, i):
        print(c)
