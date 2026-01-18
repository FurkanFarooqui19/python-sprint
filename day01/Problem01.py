# Build a program that:
# Takes two numbers
# Prints:
# Their sum
# Their difference
# Their product
# The bigger number

# Solution:

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(x + y)
print(x - y)
print(x * y)
print(x if x > y else y)