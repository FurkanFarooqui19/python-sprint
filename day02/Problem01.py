# Write a program that takes an integer n and:
# - checks whether the number is positive, negative, or zero,
# - if the number is positive, check whether it is even or odd.

# Solution:

n = int(input("Enter a number: "))

if n > 0:
    print(f"{n} is a Positive Number")
    if n%2 == 0:
        print(f"{n} is an Even Number")
    else:
        print(f"{n} is an Odd Number")
elif n == 0:
    print(f"{n} is zero")
else:
    print(f"{n} is a Negative Number")