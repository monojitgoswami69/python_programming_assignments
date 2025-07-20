#4. Write a program that takes the input until ‘q’ and print the palindrome numbers

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q': break
    if user_input == user_input[::-1]: print(user_input, "is a palindrome.")
    else: print(user_input, "is not a palindrome.")
