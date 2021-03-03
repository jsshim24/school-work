"""
Assignment #2, Problem 4
Jun Seob Shim

"""

#the following line would cause a syntax error because I didn't delimit the string that I'm attempting to print
#print(--------------------------------------------------------------)

#printing title
print("--------------------------------------------------------------")
print("\t\tmL Conversion Calculator")
print("--------------------------------------------------------------")
print()

#how many mL?
ml = int(input("How many mL would you like to convert? "))

#the following line would cause a runtime error because I specified the wrong data type for the format function
#print(format(ml,".2s"),"mL ...")

print(format(ml,".2f"),"mL ...")
print()

#calculations
tsp = ml * 0.202884
tbsp = tsp / 3

#the following line would cause a logic error because I used the wrong operator for conversion
#ul = ml / 1000

ul = ml * 1000
nl = ml * 1000000

#formatted values (commas and decimal places)
ftsp = format(tsp,",.2f")
ftbsp = format(tbsp,",.2f")

#the following line would cause a logic error because I specified the wrong variable to format
#ful = format(nl,",.2f")

ful = format(ul,",.2f")
fnl = format(nl,",.2f")

#print with formatting
print(format("... in teaspoons","24s"),format(ftsp,">14s"),"tsp")
print(format("... in tablespoons","24s"),format(ftbsp,">14s"),"tbsp")
print(format("... in microliters","24s"),format(ful,">14s"),"uL")

#the following would cause a syntax error because I used different starting and ending delimiters for printing a string literal
#print(format("... in nanoliters',"24x"),format(fn1,">14s"),"nL")

print(format("... in nanoliters","24s"),format(fnl,">14s"),"nL")
