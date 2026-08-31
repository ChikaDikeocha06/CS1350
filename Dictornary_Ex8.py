# Exercise 8: Use get() for a student who may not exist

grades = {
    "Alice": 85,
    "Bob": 92,
    "Carol": 78
}

print(grades.get("Dave", "Student not found"))
