# Given a list of integers:
# - find the largest number in the list,
# - find the second largest number in the list,
# do not use built-in functions for finding maximum values.

# Solution:

n = [66, 44, 99, 55, 88, 77]

largest = n[0]
second_largest = n[0]

for i in n:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(f"{largest} is the largest number in the list")
print(f"{second_largest} is the second largest number in the list")
        