# This program is going to import CSV module to handle CSV file outputs

import csv
student_list = []
with open("student.csv") as file:
    read = csv.reader(file)
    for fName, lName in read:
        student_list.append({"first_name":fName, "last_name":lName})
        
for student in sorted(student_list, key=lambda stud:stud["first_name"]):
    print(f"First Name: {student['first_name']} || Last Name: {student['last_name']}")