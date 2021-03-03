"""
Assignment #1, Problem 3
Jun Seob Shim

I wanted to make the program more fun and decided to do a quick Google search on how to use conditional statements and how to check
if strings can be converted to numbers in Python. Sources below:

https://www.w3schools.com/python/python_conditions.asp
https://www.kite.com/python/answers/how-to-check-if-a-string-contains-only-numbers-in-python
"""

#establish number of mL (when input is disabled)
ml=250

#using input
'''uncomment from here...


#establish number of mL
stml = (input("Enter a whole number of mL to be converted to US Fluid Volume Units: "))

#attempt 1
mlboo = (stml.isdecimal())
if mlboo == True:
    ml = int(stml)
else:
    stml = input("Very funny. Positive integers only please: ")

#if false, attempt 2
mlboo = (stml.isdecimal())
if mlboo == True:
    ml = int(stml)
else:
    stml = input("Last chance! Positive integers only: ")

#if false, last attempt
mlboo = (stml.isdecimal())
if mlboo == True:
    ml = int(stml)
else:
    print("Python has run out of patience. The end.")
    quit()


...to here to enable the input part of this program. I added inputs for fun. Without the above section, the program will behave
exactly like the assignment specified.'''

#the actual assignment

#calculations
tsp = ml * 0.202884
tbsp = tsp / 3
cup = tbsp / 16
pint = cup / 2
quart = pint / 2
gallon = quart / 4
floz = ml / 29.5735

#string formatting
fml = format("mL:","16s") #ha
ftsp = format("tsp:","16s")
ftbsp = format("tbsp:","16s")
fcup = format("cup(s):","16s")
fpint = format("pint(s):","16s")
fquart = format("quart(s):","16s")
fgallon = format("gallon(s):","16s")
ffloz = format("fl oz:","16s")

#printing with specified format
print("--------------------------------------------------------------")
print("\t\tmL to US Fluid Volume Units")
print("--------------------------------------------------------------")
print("\t",fml,ml, sep="")
print("\t",ftsp,tsp, sep="")
print("\t",ftbsp,tbsp, sep="")
print("\t",fcup,cup, sep="")
print("\t",fpint,pint, sep="")
print("\t",fquart,quart, sep="")
print("\t",fgallon,gallon, sep="")
print("\t",ffloz,floz,sep="")
print("--------------------------------------------------------------")
