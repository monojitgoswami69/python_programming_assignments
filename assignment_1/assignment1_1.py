#1. Write a program that asks the number of years as input, and then prints out the number of days, hours, minutes, and seconds in that number of years. Assume 365 days per year, and also check an year for leap year or not.

year = int(input("Enter number of years: "))
y = int(input("Enter year to check for: "))
days = year * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"In {year} year(s):")
print(f"{days} days\n{hours} hours\n{minutes} minutes\n{seconds} seconds")
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0): print(f"{y} is a Leap Year")
else: print(f"{y} is not a Leap Year")