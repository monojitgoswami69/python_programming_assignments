# 3. Write a program to take a 2-digit number and then print the reversed number. That is, if the input given is 25, the program should print 52. Then extend it for 3-digit number and also check for odd and even

num = (input("Enter a 2 or 3-digit number: ")
print(f"Reversed: {(num)[::-1]}")
print(f"{num} is {'Even' if int(num) % 2 == 0 else 'Odd'}")
