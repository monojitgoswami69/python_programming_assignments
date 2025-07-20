'''
6. Write a program to print an inverted triangle of stars
*********
 *******
  *****
   ***
    * 
'''
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2*i - 1))
