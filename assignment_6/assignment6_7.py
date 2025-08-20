# 7. Write a program to implement the Tower of Hanoi problem.

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    else:
        moves = 0
        moves += tower_of_hanoi(n-1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        moves += 1
        moves += tower_of_hanoi(n-1, auxiliary, destination, source)
        return moves

n = int(input("Enter the number of disks: "))
if n <= 0:
    print("Number of disks must be positive!")
    exit()

print(f"\nSolving Tower of Hanoi with {n} disks:")
total_moves = tower_of_hanoi(n, 'A', 'C', 'B')
print(f"\nTotal moves required: {total_moves}")
