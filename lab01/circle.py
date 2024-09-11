import math

radius = input("please enter a number of your choice (in integer) as the radius of a circle:")
r = int(radius)

perimeter1 = 2 * r * math.pi
perimeter = round(perimeter1, 2)

area1 = r ** 2 * math.pi
area = round(area1, 2)

print("The circle with radius " + radius + " has an area of " + str(area) + " and a perimeter of " + str(perimeter) + ".")
