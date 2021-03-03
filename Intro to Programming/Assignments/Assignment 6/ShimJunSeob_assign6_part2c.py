"""
Assignment #6, Part 2c
Jun Seob Shim
5/11/2020
Intro to Programming Section 012
Print Any Number

Sources:
Using variables in function names:
https://stackoverflow.com/questions/34794634/how-to-use-a-variable-as-function-name-in-python
"""
# Line functions
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

#number functions
#print 0 with char
def number_0(width,char):
    pattern = horizontal_line(width,char) + "\n"
    for i in range(3):
        pattern += char + " "*(width-2) + char + "\n"
    pattern += horizontal_line(width,char)
    return pattern
    
#print 1 with char
def number_1(width,char):
    pattern = vertical_line(width-1,5,char)
    return pattern

#print 2 with char
def number_2(width,char):
    pattern = ""
    for i in range(5):
        if i%2 == 0:
            pattern += horizontal_line(width,char) + "\n"
        elif i == 1:
            pattern += " "*(width-1) + char + "\n"
        else:
            pattern += char + "\n"
    return pattern

#print 3 with char
def number_3(width,char):
    pattern = ""
    for i in range(5):
        if i%2 == 0:
            pattern += horizontal_line(width,char) + "\n"
        else:
            pattern += " "*(width-1) + char + "\n"
    return pattern
            
#print 4 with char
def number_4(width,char):
    pattern = two_vertical_lines(width,2,char)
    pattern += horizontal_line(width,char) + "\n"
    pattern += vertical_line(width-1,2,char)
    return pattern

#print 5 with char
def number_5(width,char):
    pattern = ""
    for i in range(5):
        if i%2 == 0:
            pattern += horizontal_line(width,char) + "\n"
        elif i == 3:
            pattern += " "*(width-1) + char + "\n"
        else:
            pattern += char + "\n"
    return pattern

#print 6 with char
def number_6(width,char):
    pattern = ""
    for i in range(5):
        if i%2 == 0:
            pattern += horizontal_line(width,char) + "\n"
        elif i == 3:
            pattern += char
            pattern += " "*(width-2) + char + "\n"
        else:
            pattern += char + "\n"
    return pattern

#print 7 with char
def number_7(width,char):
    pattern = horizontal_line(width,char) + "\n"
    pattern += vertical_line(width-1,4,char)
    return pattern

#print 8 with char
def number_8(width,char):
    pattern = ""
    for i in range(5):
        if i%2 == 0:
            pattern += horizontal_line(width,char) + "\n"
        else:
            pattern += char + " "*(width-2) + char + "\n"
    return pattern

#print 9 with char
def number_9(width,char):
    pattern = ""
    for i in range(4):
        if i%2 == 0 and i<3:
            pattern += horizontal_line(width,char) + "\n"
        elif i == 1:
            pattern += two_vertical_lines(width,1,char)
        else:
            pattern += vertical_line(width-1,2,char)
    return pattern

#print any number
def print_number(num,width,char):
    pattern = globals()['number_'+str(num)](width,char)
    print(pattern)

#test output

print_number(0, 5, '*')
print_number(1, 6, '*')
print_number(2, 7, '*')
print_number(3, 8, '*')
print_number(4, 9, '*')
print_number(5, 10, '*')
print_number(6, 11, '*')
print_number(7, 12, '*')
print_number(8, 13, '*')
print_number(9, 14, '*')
