# Write a program that:
# 1.  Reads integers from a file numbers.txt (one number per line)
# 2.  Ignores invalid lines (non-integers) using error handling
# 3.  Prints the sum of valid integers

# Solution:

total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        try:
            num = int(line.strip())
            total += num
        except ValueError:
            pass

print("Sum =", total)