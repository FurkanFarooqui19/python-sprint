# Write a Python program to print a Hollow Number Hourglass Pyramid pattern.
# Numbers decrease from the edges toward the center, spaces inside, and mirrored vertically.

# Solution:

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")

    if i != n:
        print(" " * (2 * (n - i) - 1), end="")

    if i == n:
        for j in range(n - 1, 0, -1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    print()

for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    if i != n:
        print(" " * (2 * (n - i) - 1), end="")

    if i == n:
        for j in range(n - 1, 0, -1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    print()
