grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "David": "C"
}
students_by_grade = {}
for name, grade in grades.items():
    if grade not in students_by_grade:
        students_by_grade[grade] = []
    students_by_grade[grade].append(name)
print(students_by_grade)
# Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}
