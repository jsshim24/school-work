"""
Assignment #6, Part 1
Jun Seob Shim
5/11/2020
Intro to Programming Section 012
Rectangle Simulator
"""
#function to calculate area of rectangle
def compute_area_of_rectangle(length,width):
    area = length*width
    return area

#function to calculate perimeter of rectangle
def compute_perimeter_of_rectangle(length,width):
    perimeter = 2*length + 2*width
    return perimeter

#function to print rectangle
def draw_rectangle(length,width):
    rect = ""
    #add a line to match length
    for i in range(length):
        rect += "*"*width + "\n"
    return rect

#function to get side length from user
def get_input(prompt,low,high):
    invalidinput = True

    #keep prompting user to enter a value within range
    while invalidinput:
        measurement = int(input(prompt))
        if low <= measurement and measurement <= high:
            invalidinput = False
        else:
            print("Invalid input, try again.")
    return measurement

#main body of program (copied from assignment page
#get side lengths from user between 3 and 10
length = get_input("Enter a length between 3 and 10: ", 3, 10)
width  = get_input("Enter a width between 3 and 10: ", 3, 10)

#compute area and perimeter
area  = compute_area_of_rectangle(length, width)
perim = compute_perimeter_of_rectangle(length, width)

#print area and perimeter
print ("Area:", area, "; Perim:", perim)

#draw rectangle as printed stars
rect = draw_rectangle(length, width)
print (rect)
