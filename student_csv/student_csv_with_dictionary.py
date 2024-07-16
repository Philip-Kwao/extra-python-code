# This program is going to read a csv file and sort them in an ascending order

student_list = []

with open("student.csv") as file:
    for line in file:
        fName, lName = line.rstrip().split(",")
        student_dict = {"first_name":fName, "last_name":lName}
        student_list.append(student_dict)

# def stud():
#     return student_dict["first_name"]

for student in sorted(student_list, key=lambda stud:stud["first_name"]):
    print(f"First Name: {student['first_name']} || Last Name: {student['last_name']}")