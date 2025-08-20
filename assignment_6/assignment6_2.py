# 2. Write a function to return a list of ten consecutive integers.

def get_consecutive_integers(start_num):
    return [start_num + i for i in range(10)]

start = int(input("Enter the starting number: "))
consecutive_list = get_consecutive_integers(start)
print(f"Ten consecutive integers starting from {start}:")
print(consecutive_list)
