#Student ID Checker

import re

stud_id = input("Please enter your Student ID: ")

pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, stud_id):
    print("Student ID is valid")
else:
    print("Student ID is not valid")