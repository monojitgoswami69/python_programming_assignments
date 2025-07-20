#1. A store charges Rs120 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is Rs100 per item. If you buy 100 or more items, the cost is Rs70 per item. Write a program that asks the user how many items they are buying and prints the total cost.

items = int(input("Enter number of items: "))
if items < 10: cost = 120
elif items <= 99: cost = 100
else: cost = 70
total = items * cost
print(f"Total cost is Rs {total}")