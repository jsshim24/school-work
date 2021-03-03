"""
Assignment #5, Part 4
Jun Seob Shim
15/10/2020
Intro to Programming Section 012
Table Madness
"""

#print intstructions
print("Instructions: choose which table you would like to build.")
print("Then enter the number of rows and columns that you would\nlike present in the selected table.")
print()
print("\t1. Addition Table")
print("\t2. Subtraction Table")
print("\t3. Multiplication Table")
print()

#ask which table
invalidtable = True

while invalidtable:
    table = int(input("Which table would you like to work with?: "))
    if 0 < table < 4:
        invalidtable = False
        print()
    else:
        print("Invalid table type, try again.")

#ask how many rows
invalidrows = True

while invalidrows:
    rows = int(input("Enter # of rows: "))
    if rows > 0:
        invalidrows = False
    else:
        print("Invalid # of rows, try again.")

#ask how many columns
invalidcolumns = True

while invalidcolumns:
    columns = int(input("Enter # of columns: "))
    if columns > 0:
        invalidcolumns = False
    else:
        print("Invalid # of columns, try again.")



