"""
Assignment #4, Part 2, Part a
Jun Seob Shim
8/10/2020
Intro to Programming Section 012
Pick up sticks (single player)
"""
#ask user for number of sticks
invalidsticks = True

while invalidsticks:
    sticks = int(input("How many sticks (10-100)? "))
    if sticks < 10:
        print("Sorry, that's too few sticks. Try again.")
    elif sticks > 100:
        print("Sorry, that's too many sticks. Try again.")
    else:
        print("Great, Let's play ...")
        invalidsticks = False
        print()

#play game (while there are sticks on the table)
while sticks > 0:    
    invalidnumsticks = True

    #ask user for valid number of sticks to take
    while invalidnumsticks:
        if sticks == 1:
            print("There is 1 stick on the table.")
        else:
            print("There are",sticks,"sticks on the table.")
        numsticks = int(input("How many sticks do you want to take (1, 2, or 3)? "))
        if 1 <= numsticks <= 3:
            #if the inputted number would leave a negative amount of sticks; invalid
            if sticks - numsticks < 0:
                print("Sorry, that would bring the total # of sticks below 0. Try again.")
            else:
                sticks -= numsticks
                invalidnumsticks = False
            print()
        else:
            print("Sorry, that's not a valid number.")
            print()

#when there are no sticks left    
print("There are no sticks left on the table! Game over.")
