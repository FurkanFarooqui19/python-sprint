# 1.  Problem: Given a list of integers, create a new list containing only unique elements,
# preserving original order.
# Input:
# [1, 2, 2, 3, 1, 4]
# Output:
# [1, 2, 3, 4]
# Constraints:
# Do not use set() directly for final output.

# Solution:

old = [1, 2, 2, 3, 1, 4]
new = []
seen = set()

for ele in old:
    if ele not in seen:
        new.append(ele)
        seen.add(ele)

print(new)