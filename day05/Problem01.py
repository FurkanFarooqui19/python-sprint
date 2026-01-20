# Write a function count_digits(n) that returns the number of digits in a positive
# integer using recursion only.
# Input:
# count_digits(54321)
# Output:
# 5
# Rules:
# No loops
# No string conversion
# Use only recursion and basic arithmetic

# Solution:

def count_digits(n):
    if n < 10:
        return 1
    return (1 + count_digits(n//10))

print(count_digits(54321))