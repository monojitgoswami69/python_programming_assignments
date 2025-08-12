# 2. Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should equal [4,6,13]

L = list(map(int, input("Enter the elements of list L: ").split()))
M = list(map(int, input("Enter the elements of list M: ").split()))
if len(L) != len(M):
    print("Error: Lists must be of the same length.")
else:
    N = [L[i] + M[i] for i in range(len(L))]
    print(N)

