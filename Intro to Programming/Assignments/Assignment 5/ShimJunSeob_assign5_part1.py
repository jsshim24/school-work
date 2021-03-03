"""
Assignment #5, Part 1
Jun Seob Shim
15/10/2020
Intro to Programming Section 012
Pizza Party
"""
import math

#get starting values from user
budget = int(input("Enter budget for your party: "))
slicec = float(input("Cost per slice of pizza: "))
piec = float(input("Cost per whole pizza pie (8 slices): "))
people = int(input("How many people will be attending your party? "))
totalslices = 0

#ask each person how many slices
for i in range(people):
    invalidslices = True
   
    while invalidslices:
        print("Enter number of slices for person #",i+1,sep="",end="")
        slices = int(input(": "))
        
        if slices > 0:
            invalidslices = False
            
        else:
            print("Not a valid entry, try again!")
            print()

    #sum slices to find total number of slices
    totalslices += slices

#calculate total cost
totalcost = piec * math.floor(totalslices/8) + slicec * (totalslices % 8)

#post calculation part 1, advise how to buy
if budget - totalcost >= 0:
    print("You should purchase",math.floor(totalslices/8),"pies and",totalslices % 8,"slices")
    print("Your total cost will be:",format(totalcost,".2f"))
else:
    print("Your order cannot be completed.")
    print("You would need to purchase",math.floor(totalslices/8),"pies and",totalslices % 8,"slices")

#post calculation part 2, print how much money left over
if budget - totalcost == 0:
    print("You will have no money left after your order")
elif budget - totalcost > 0:
    print("You will still have",format(budget-totalcost,".2f"),"left after your order")
else:
    print("This would put you overbudget by",format(abs(budget-totalcost),".2f"))

    



