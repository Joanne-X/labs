import math

side1 = input("please enter a number of your choice (in integer):")
x = int(side1)

side2 = input("please enter another number of your choice (in integer):")
y = int(side2)

x_2 = x ** 2
y_2 = y ** 2
sumofxy_2 = x_2 + y_2
hypotheuse = math.sqrt(sumofxy_2)

print("The hypotheuse is " + str(hypotheuse) + ".")
