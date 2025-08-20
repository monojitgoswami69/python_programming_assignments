# 1. Write a menu driven program to find out the area of circle, square, rectangle and triangle.

import math

def area_circle(radius):
    return math.pi * radius * radius

def area_square(side):
    return side * side

def area_rectangle(length, breadth):
    return length * breadth

def area_triangle(base, height):
    return 0.5 * base * height

while True:
    print("\n--- Area Calculator ---")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")
    choice = input("Selection (1-5): ")
    match choice:
        case '1':
            radius = float(input("Enter radius of circle: "))
            print(f"Area of circle = {area_circle(radius):.2f}")
        case '2':
            side = float(input("Enter side of square: "))
            print(f"Area of square = {area_square(side):.2f}")
        case '3':
            length = float(input("Enter length of rectangle: "))
            breadth = float(input("Enter breadth of rectangle: "))
            print(f"Area of rectangle = {area_rectangle(length, breadth):.2f}")
        case '4':
            base = float(input("Enter base of triangle: "))
            height = float(input("Enter height of triangle: "))
            print(f"Area of triangle = {area_triangle(base, height):.2f}")
        case '5':
            break
        case _:
            print("Invalid choice!")
