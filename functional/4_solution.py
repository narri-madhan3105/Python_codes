import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(3)

print("Area: ", a, "Circumference: ", c)
#print(“area:”,round(a,2),”circumference”,round(b,2))
#for rounding off upto 2 digits