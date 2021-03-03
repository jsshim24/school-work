"""
Assignment #3, Problem 1
Jun Seob Shim
9/29/2020
Intro to Programming Section 012
ShimJunSeob_assign3_problem1.py

Sources:
Math ceiling function: https://stackoverflow.com/questions/26454649/python-round-up-to-the-nearest-ten
"""
#import modules
import turtle
import math

#title
print("Valid Triangle Tester")
print()

#get co-ordinates from user
x1 = float(input("Enter Point #1 - x position: "))
y1 = float(input("Enter Point #1 - y position: "))

x2 = float(input("Enter Point #2 - x position: "))
y2 = float(input("Enter Point #2 - y position: "))

x3 = float(input("Enter Point #3 - x position: "))
y3 = float(input("Enter Point #3 - y position: "))

#compute and print length of sides
side1 = round(((x1-x2)**2 + (y1-y2)**2)**0.5,2)
side2 = round(((x3-x1)**2 + (y3-y1)**2)**0.5,2)
side3 = round(((x2-x3)**2 + (y2-y3)**2)**0.5,2)

print()
print("The length of each side of your test shape is:")
print()

print("Side 1:", format(side1,".2f"))
print("Side 2:", format(side2,".2f"))
print("Side 3:", format(side3,".2f"))
print()

#compare side lengths to determine valid triangle
if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print("This is a valid triangle!")
    
    if side1==side2==side3:
        print("This is an equilateral triangle")
        
    elif side1==side2 or side2==side3 or side3==side1:
        print("This is an iscosceles triangle")
        
    else:
        print("This is a scalene triangle")

#determine canvas size needed (still nested in if statement)
    csize = abs(x1)

    if csize < abs(y1):
        csize = y1

    if csize < abs(x2):
        csize = x2

    if csize < abs(y2):
        csize = y2

    if csize < abs(x3):
        csize = x3

    if csize < abs(y3):
        csize = y3

    csize = (math.ceil(csize/10)*10)*2 + 100

#establish canvas and draw x, y axes
    turtle.setup(csize,csize)
    turtle.goto(0,csize/2)
    turtle.pendown()
    turtle.goto(0,-1*(csize/2))
    turtle.penup()
    turtle.goto(csize/2,0)
    turtle.pendown()
    turtle.goto(-1*(csize/2),0)
    turtle.penup()

#determine pen color based on triangle type
    if side1==side2==side3:
        turtle.pencolor("green")
        
    elif side1==side2 or side2==side3 or side3==side1:
        turtle.pencolor("blue")
        
    else:
        turtle.pencolor("red")

#draw triangle        
    turtle.pensize(2)
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x1,y1)

else:
    print("This is not a valid triangle")
