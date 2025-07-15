""" 2. Write a program to calculate the amount payable after simple and compound interest. 
Simple Interest = (P ⋆ t ⋆ r) / 100. 
Compound Interest = P ⋆ ((1 + r / 100)^t - 1)
"""

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time in years: "))
simple_interest = (p * r * t) / 100
compound_interest = p * ((1 + r / 100)**t - 1)
print(f"Simple Interest = {simple_interest:.2f}")
print(f"Net amount payable after Simple Interest = {simple_interest + p:.2f}")
print(f"Compound Interest = {compound_interest:.2f}")
print(f"Net amount after Compound Interest = {simple_interest + p:.2f}")