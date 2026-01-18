# 2.  Problem: You are given a list of dictionaries representing students.
# students = [
#  {"name": "A", "marks": 85},
#  {"name": "B", "marks": 72},
#  {"name": "C", "marks": 85},
#  {"name": "D", "marks": 90}
# ]
# Tasks:
# 1.  Find the highest marks
# 2.  Print names of all students who scored the highest
# 3.  Store result in a dictionary like:
# {
#  "top_score": 90,
#  "students": ["D"]
# }
# Rules:
# No built-in max ()
# Must use loops, conditions, and dictionaries

# Solution:

students = [
 {"name": "A", "marks": 85},
 {"name": "B", "marks": 72},
 {"name": "C", "marks": 85},
 {"name": "D", "marks": 90}
]

top_score = 0

top_students = []
for student in students:
    if student["marks"] > top_score:
        top_score = student["marks"]

for student in students:
    if student["marks"] == top_score:
        top_students.append(student["name"])
        
result = {
    "top_score": top_score,
    "students": top_students
}

print(result)