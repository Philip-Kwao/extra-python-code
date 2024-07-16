# This program is going to write into the csv file the users friends first and last names.

import csv

fName = input("First Name: ")
lName = input("Last Name: ")

with open("friend.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["first_name","last_name"])
    write.writerow({"first_name":fName, "last_name":lName})