# How to read CSV File
students = []

with open("student.csv") as file:
    for line in file:
        fName,lName = line.capitalize().rstrip().split(",")
        # print(f"The first name is {fName} and the last name is {lName}")
        students.append(f"First Name: {fName} || Last Name: {lName}")
        sorted(students)
for student in sorted(students):
    print(student)