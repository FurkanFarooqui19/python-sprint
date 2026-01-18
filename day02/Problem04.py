# Write a program that takes a number n and:
# - prints all numbers from 1 to n,
# - skips numbers that are divisible by 4,
# - stops the loop completely if a number divisible by 10 is encountered

# Solution:

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 10 == 0:
        break
    if i % 4 == 0:
        continue
    print(i)
