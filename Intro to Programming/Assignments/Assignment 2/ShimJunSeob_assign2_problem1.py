"""
Assignment #2, Problem 1
Jun Seob Shim
"""

#getting user input values
print("This program will project how much you can earn by investing money in a high-\nyield savings account over a 3 month period.")

print()

start = float(input("To begin, enter how much money you would like to initially invest (i.e. 500):\n"))
interest = float(input("Next, enter your projected annual interest rate. For example, enter 5 for 5%:\n"))

#calculations
m1interest = round(start*(interest/1200),2)
m1end = start+m1interest

m2interest = round(m1end*(interest/1200),2)
m2end = m1end+m2interest
    
m3interest = round(m2end*(interest/1200),2)
m3end = m2end+m3interest

#formatting results to 2 decimal places
fstart1 = format(start,",.2f")
finterest1 = format(m1interest,",.2f")
fend1 = format(m1end,",.2f")
finterest2 = format(m2interest,",.2f")
fend2 = format(m2end,",.2f")
finterest3 = format(m3interest,",.2f")
fend3 = format(m3end,",.2f")

#printing results with string formatting
print()
print("------- Calculating --------")
print()

print("Month","Starting Balance    ","Interest  ","Ending Balance")
print(format("1","5s"),format(fstart1,"20s"),format(finterest1,"10s"),fend1)
print(format("2","5s"),format(fend1,"20s"),format(finterest2,"10s"),fend2)
print(format("3","5s"),format(fend2,"20s"),format(finterest3,"10s"),fend3)
