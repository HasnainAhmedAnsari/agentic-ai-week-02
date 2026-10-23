
import json

# Task 11: JSON student object
student_json = """
{
    "name": "Ali",
    "marks": 85,
    "program": "BSCS"
}
"""

# Convert JSON text into a Python dictionary
student = json.loads(student_json)

print("TASK 11: JSON OBJECT")
print("Name:", student["name"])
print("Marks:", student["marks"])
print("Program:", student["program"])

# Equivalent Python dictionary
student_dict = {
    "name": "Ali",
    "marks": 85,
    "program": "BSCS"
}

print("\nEquivalent Python dictionary:")
print(student_dict)

# Task 12: JSON array containing three students
students_json = """
[
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Ahmed"}
]
"""

students = json.loads(students_json)

print("\nTASK 12: STUDENT ARRAY")

for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}")

# Convert Python data back into JSON
print("\nPython dictionary converted to JSON:")
print(json.dumps(student_dict, indent=2))
