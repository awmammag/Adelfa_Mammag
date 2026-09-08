#Finding the Hypotenuse of a Right Triangle Using the Math Library
import math

#inputting the sides of a and b
a = float(input("Enter length of the first shorter side "))
b = float(input("Enter length of the second shorter side "))

#processing/ calculating the hypotenuse
c = math.sqrt(pow(a, 2 ) + pow(b, 2))

#output/ displaying the hypotenuse
print(f"Hypotenuse is  {c:.2f}")


