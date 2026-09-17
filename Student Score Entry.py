
try:
    age = int(input("Please enter your age: "))
    if 0<= age <= 100:
        print("Valid age: ", age)
    else: print("Invalid age. Please enter a valid age")
except ValueError:
    print("Invalid age. Input a whole number")