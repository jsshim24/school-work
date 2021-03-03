"""
Assignment #11, Part 1
Jun Seob Shim
10/12/2020
Intro to Programming Section 012
Rectangles
"""

#define class
class Rectangle:
    #constructor function with inputs
    def __init__(self,width,length,x,y):
        self.width = width
        self.length = length
        self.x = x
        self.y = y

    #get area function
    def get_area(self):
        area = self.width*self.length
        return area

    #get perimeter function
    def get_perimeter(self):
        perimeter = 2*self.width + 2*self.length
        return perimeter

#define 2 rectangles
rect1 = Rectangle(10,15,5,3)
rect2 = Rectangle(3,5,15,7)

#print first rectangle info
print("Rectangle #1")
print("* Coordinates: ("+str(rect1.x)+", "+str(rect1.y)+")")
print("* Area: "+str(rect1.get_area()))
print("* Perimeter: "+str(rect1.get_perimeter()))

#print spacing
print()

#print second rectangle info
print("Rectangle #2")
print("* Coordinates: ("+str(rect2.x)+", "+str(rect2.y)+")")
print("* Area: "+str(rect2.get_area()))
print("* Perimeter: "+str(rect2.get_perimeter()))
