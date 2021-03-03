"""
Assignment #4, Part 1
Jun Seob Shim
8/10/2020
Intro to Programming Section 012
Roll the Dice

Sources:
Using multiple argument in if statement using "or":
https://discuss.codecademy.com/t/can-we-compare-one-value-with-multiple-values-using-or/349398
"""
#import modules
import random as r

#get number of dice sides from user
invalidsides = True

while invalidsides:
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
    if sides == 4 or sides == 6 or sides == 8 or sides == 10 or sides == 12 or sides == 20:
        invalidsides = False
        print()
        print("Thanks, here we go!")
    else:
        print("Invalid size, try again.")

#establish variables for dice rolling
notsnakeeyes = True
die1total = 0
die2total = 0
rolls = 0

#special roll counters
doubles = 0
high = 0
highlow = 0
evens = 0
odds = 0
sums = 0

while notsnakeeyes:
    #dice values
    die1 = r.randint(1,sides)
    die2 = r.randint(1,sides)
    #counter values
    die1total += die1
    die2total += die2
    rolls += 1

    print("\n", rolls, ". die #1 is ","*",die1,"* ","and die #2 is ","*",die2,"* ",sep="",end="")

    #doubles
    if die1 == die2:
        print("Doubles! ", end="")
        doubles += 1

    #high
    if die1 == die2 == sides:
        print("High! ", end="")
        high += 1

    #highlow    
    if (die1 == 1 and die2 == sides) or (die1 == sides and die2 == 1):
        print("High/Low! ", end="")
        highlow += 1

    #evens    
    if die1 % 2 == 0 and die2 % 2 == 0:
        print("Evens! ", end="")
        evens += 1

    #odds    
    if die1 % 2 != 0 and die2 % 2 != 0:
        print("Odds! ", end="")
        odds += 1

    #sums   
    if die1 + die2 == sides:
        print("Sum value is size value! ", end="")
        sums += 1

    #snakeeyes   
    if die1 == 1 and die2 == 1:
        print("Snake Eyes! ", end="")
        notsnakeeyes = False

print()
print()

print("You finally got snake eyes on roll #",rolls)

#print counters for special rolls
print("Along the way you rolled DOUBLES ",doubles," time(s). (",format((doubles/rolls)*100,".2f"),"% of all rolls were doubles)\
",sep="")
print("Along the way you rolled TWO HIGH VALUES ",high," time(s). (",format((high/rolls)*100,".2f"),"% of all rolls were two \
high values)",sep="")
print("Along the way you rolled TWO EVENS ",evens," time(s). (",format((evens/rolls)*100,".2f"),"% of all rolls were two evens)\
",sep="")
print("Along the way you rolled TWO ODDS ",odds," time(s). (",format((odds/rolls)*100,".2f"),"% of all rolls were two odds)",sep="")
print("Along the way you rolled HIGH / LOW ",highlow," time(s). (",format((highlow/rolls)*100,".2f"),"% of all rolls were high/low)\
",sep="")
print("Along the way you rolled A SUM VALUE ",sums," time(s). (",format((doubles/rolls)*100,".2f"),"% of all rolls were \
a sum value)",sep="")

#print average roll
print("Average roll for die #1:",format(die1total/rolls,".2f"))
print("Average roll for die #2:",format(die2total/rolls,".2f"))
