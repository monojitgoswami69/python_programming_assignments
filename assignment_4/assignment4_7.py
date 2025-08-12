# 7. Write a program to compare two equal sized lists and print the first index where they differ

list1 = list(map(int, input("Enter the numbers for the first list: ").split()))
list2 = list(map(int, input("Enter the numbers for the second list: ").split()))
if len(list1) != len(list2):
    print("Lists are not of the same size.")
else:
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print(f"Lists first differ at index {i}")
            break
    else:
        print("Lists are identical.")
