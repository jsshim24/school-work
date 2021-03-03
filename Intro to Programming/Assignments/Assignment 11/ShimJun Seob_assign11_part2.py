"""
Assignment #11, Part 2
Jun Seob Shim
10/12/2020
Intro to Programming Section 012
Gumball Machine
"""
#import random module
import random

#define class
class Gumball_Machine:
    def __init__(self,balls):
        #set up capacity
        self.capacity = balls

        #set up money counter
        self.money= 0.00

        #create empty list of gumballs
        self.gumballs = []

        #iterate over capacity
        for i in range(self.capacity):
            #get random integer to determine colour of gumball added
            colour = random.randint(1,3)

            #if statement to append different gumballs
            if colour == 1:
                self.gumballs.append("red")

            elif colour == 2:
                self.gumballs.append("green")

            else:
                self.gumballs.append("blue")

        #announce success
        print("Gumball Machine created with "+str(self.capacity)+" random gumballs")
        print()

    #define machine report function
    def report(self):
        print("Gumball Machine Report:")

        #print how many gumballs
        print("* Gumballs in machine: "+str(len(self.gumballs)))

        #print how much money (formatted)
        print("* Money in machine: $"+format(self.money,".2f"))
        print()

    #define dispense gumball
    def dispense(self,coin):
        
        #if the coin is a quarter
        if coin == 0.25:
            
            #if there are gumballs in the machine
            if len(self.gumballs) > 0:
                
                #print acceptance and dispense first element in list
                print("Accepting 0.25; Dispensing a "+self.gumballs[0]+" gumball")

                #delete first elemenet in list
                del self.gumballs[0]

                #add to money counter
                self.money += 0.25

            #if there are no gumballs
            else:
                print("Machine is empty, no gumball will be dispensed")

        #if the coin isn't a quarter
        else:
            print("Invalid coin, no gumball will be dispensed")

        #print spacing
        print()

    #define count gumballs
    def count_gumballs_by_type(self,color):

        #if there are gumballs of that colour
        if (color in self.gumballs) == True:

            #define counter
            counter = 0

            #iterate through list
            for i in range(len(self.gumballs)):

                #if the list element is that colour
                if self.gumballs[i] == color:

                    #add to counter
                    counter += 1

            #print final result
            print("There are "+str(counter)+" gumballs of type "+color+" in the machine")

        #if there are no gumballs of that colour
        else:

            #print no gumballs
            print("There are 0 gumballs of type "+color+" in the machine")

        #print for spacing
        print()

#tester code
machine = Gumball_Machine(5)
machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
