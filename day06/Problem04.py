# Write a Python program to print a butterfly pattern using numbers instead of stars.

# Solution:

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    
    print(" " * (2*(n - i)), end="")
    
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    
    print(" " * (2*(n - i)), end="")
    
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()
