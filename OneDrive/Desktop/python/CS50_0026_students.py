# Hare krishna

import csv
students = []

with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
       
        students.append({"name": row[0], "house": row[1]})



for student in sorted(students, key=lambda student: student["name"]):#ananymous function
    print(f"{student['name']} is {student['house']}")