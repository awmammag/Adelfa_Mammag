# ANGEL GRACE MAMMAG
#8-ADELFA

num1 = int(input("Enter the first number ")) #Global variable
num2 = int(input("Enter the second number ")) #Global variable

def calculate_sum():
    sum = (num1 + num2) #local variable
    print ("The sum is", sum)

def calculate_difference():
    difference = (num1 - num2) #local variable
    print ("The difference is", difference)

calculate_sum()
calculate_difference()
