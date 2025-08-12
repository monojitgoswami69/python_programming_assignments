# 4. Write a program to read two lists num and denum which contain the numerators and denominators of the same fractions at the respective indexes. Then display the smallest and largest fraction along with its index.

num = list(map(int, input("Enter the numerators: ").split()))
denum = list(map(int, input("Enter the denominators: ").split()))

if len(num) != len(denum):
    print("Error: Lists must be of the same length.")
else:
    fractions = [n / d for n, d in zip(num, denum) if d != 0]
    if not fractions:
        print("Error: Denominator cannot be zero.")
    else:
        min_fraction = min(fractions)
        max_fraction = max(fractions)
        print(f"Smallest fraction: {min_fraction} at index {fractions.index(min_fraction)}")
        print(f"Largest fraction: {max_fraction} at index {fractions.index(max_fraction)}")
