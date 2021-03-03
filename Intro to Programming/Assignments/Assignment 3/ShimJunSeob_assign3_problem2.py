"""
Assignment #3, Problem 2
Jun Seob Shim
9/29/2020
Intro to Programming Section 012
ShimJunSeob_assign3_problem2.py
"""
#import random module
import random

#establish secret number
secnum = random.randint(1,10)
print("I'm thinking of a number between 1 and 10!")

#first try
guess = int(input("What's your guess? "))

#first try right
if guess == secnum:
    print("You got it!")
    print("The secret number was ",secnum,".",sep="")
    print("It took you 1 try to guess the number.")

#first try wrong
else:
    #first too high or low
    if guess > secnum:
        print("Too high, try again.")
    else:
        print("Too low, try again.")

    #second try
    guess = int(input("What's your guess? "))

    #second try right
    if guess == secnum:
        print("You got it!")
        print("The secret number was ",secnum,".",sep="")
        print("It took you 2 tries to guess the number.")
        
    #second try wrong
    else:
        #second too high or low
        if guess > secnum:
            print("Too high, try again.")
        else:
            print("Too low, try again.")
            
        #third try
        guess = int(input("What's your guess? "))

        #third try right
        if guess == secnum:
            print("You got it!")
            print("The secret number was ",secnum,".",sep="")
            print("It took you 3 tries to guess the number.")

        #third try wrong
        else:
            print("The secret number was ",secnum,".",sep="")
            print("You didn't guess the number.")
