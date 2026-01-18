# Write a program that:
# Takes total marks and obtained marks
# Calculates percentage
# Prints:
# Percentage
# Pass if ≥ 40 else Fail

# Solution:

Total_marks = int(input("Enter Total Marks: "))
Obtained_marks = int(input("Enter Marks Obtained: "))

Percentage = (Obtained_marks/Total_marks) * 100

print(Percentage)
print("Pass" if Percentage >= 40 else "fail")