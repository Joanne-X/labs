import math

x = input("please enter a distance or a weight amount with unit to begin (space between number and value is needed)")

n = [int (i) for i in x.split() if i.isdigit()][0]

y = x [-2:]

if y == "cm":
    m = n * 0.393701 #in
    z = round(m, 2)
    print(str(n) + " cm = " + str(z) + " in")
elif y == "in":
    m = n * 2.54     #cm
    z = round(m, 2)
    print(str(n) + " in = " + str(z) + " cm")
elif y == "yd":
    m = n * 0.9144   #m
    z = round(m, 2)
    print(str(n) + " yd = " + str(z) + " m")
elif y == " m":
    m = n * 1.09361  #yd
    z = round(m, 2)
    print(str(n) + " m = " + str(z) + " yd")
elif y == "oz":
    m = n * 28.3495  #gm
    z = round(m, 2)
    print(str(n) + " oz = " + str(z) + " gm")
elif y == "gm":
    m = n * 0.035274
    z = round(m, 2)
    print(str(n) + " gm = " + str(z) + " oz")
elif y == "lb":
    m = n * 0.453592
    z = round(m, 2)
    print(str(n) + " lb = " + str(z) + " kg")
elif y == "kg":
    m = n * 2.20462
    z = round(m, 2)
    print(str(n) + " kg = " + str(z) + " lb")
