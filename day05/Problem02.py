# Write a recursive function is_palindrome(n) that returns True if a number is a
# palindrome, else False.
# Input:
# is_palindrome(12321)
# Output:
# True
# Constraints:
# No loops
# No string conversion
# No global variables
# Must use recursion

# Solution:

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n//10, rev*10+n%10)

def is_palindrome(n):
    if n < 0:
        return False
    return n == reverse_num(n)

print(is_palindrome(12321))
print(is_palindrome(12345))