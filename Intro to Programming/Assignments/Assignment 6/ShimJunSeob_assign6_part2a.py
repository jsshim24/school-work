"""
Assignment #6, Part 2a
Jun Seob Shim
5/11/2020
Intro to Programming Section 012
Lines
"""
#return and store horizontal line of char
def horizontal_line(width,char):
    line = char*width
    return line

#return and store vertical line of char (shifted)
def vertical_line(shift,height,char):
    line = ""
    for i in range(height):
        line += " "*shift + char + "\n"
    return line

#return 2 vertical lines of char, shifted by width
def two_vertical_lines(width,height,char):
    line = ""
    for i in range(height):
        line += char + " "*(width-2) + char + "\n"
    return line

#main program (test)
print ("Horizontal line, width = 5:")
temp = horizontal_line(5, '*')
print (temp)
print ()

print ("Horizontal line, width = 10:")
temp = horizontal_line(10, '+')
print (temp)
print ()

print ("Horizontal line, width = 15:")
temp = horizontal_line(15, 'z')
print (temp)
print ()

print ("Vertical Line, shift=0; height=3:")
temp = vertical_line(0, 3, '!')
print (temp)
print ()

print ("Vertical Line, shift=3; height=3:")
temp = vertical_line(3, 3, '&')
print (temp)
print ()

print ("Vertical Line, shift=6; height=5:")
temp = vertical_line(6, 5, '$')
print (temp)
print ()

print ("Two Vertical Lines, width=3; height=3:")
temp = two_vertical_lines(3, 3, '^')
print (temp)
print ()

print ("Two Vertical Lines, width=4; height=5:")
temp = two_vertical_lines(4, 5, '@')
print (temp)
print ()

print ("Two Vertical Lines, width=5; height=2:")
temp = two_vertical_lines(5, 2, '#')
print (temp)
print ()
