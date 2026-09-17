#Grade checker

grade = int(input("Please enter your grade: "))

if 0 <= grade <= 100:
    print("Valid Grade:", grade)
else:
    print("Invalid Grade")