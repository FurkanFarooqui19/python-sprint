# Write a Python program to print a hollow diamond of stars with odd rows and even rows containing
# spaces

# Solution:

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*", end="")
    if i > 1:
        print(" " * (2*i - 3) + "*", end="")
    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*", end="")
    if i > 1:
        print(" " * (2*i - 3) + "*", end="")
    print()

