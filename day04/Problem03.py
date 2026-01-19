# Create a dictionary to store student names as keys and their marks as values.
# Write a program to:
# Add a new student
# Update marks of an existing student
# Print all students who scored more than a given value

# Solution:

student = {
    "Rahul": 90,
    "Raj": 75
}

student["Ajay"] = 89

student["Rahul"] = 88

for name, marks in student.items():
    if marks > 75:
        print(name, marks)