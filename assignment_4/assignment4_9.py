# 9. Write a function to search a number in a list

def search(lst, target):
    found = False
    for i in range(len(lst)):
        if lst[i] == target:
            print(f"{target} found at index {i}")
            found = True
    if not found:
        print("Number not found")
lst = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the number to search for: "))
search(lst, target)