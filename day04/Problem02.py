# Given two lists with duplicate values:
# Convert both lists into sets
# Find the common elements between them
# Find elements that are only present in the first set

# Solution:

l1 = [33, 44, 55, 66, 22]
l2 = [44, 55, 67, 76, 87]

s1 = set(l1)
s2 = set(l2)

print(s1 & s2)
print(s1 - s2)