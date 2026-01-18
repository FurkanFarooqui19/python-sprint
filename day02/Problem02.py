# Write a program that takes a number n and:
# - prints numbers from 1 to n,
# - prints "Fizz" for numbers divisible by 3,
# - prints "Buzz" for numbers divisible by 5,
# - prints "FizzBuzz" for numbers divisible by both 3 and 5,
# - prints the number itself if none of the above conditions are true.

# Solution:

n = int(input("Enter a number: "))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)