"""
Assignment #6, Part 2g
Jun Seob Shim
5/11/2020
Intro to Programming Section 012
Problem Practice
"""
import myfunctions
import random

#ask user for number of problems
invalidproblems = True
while invalidproblems:
    problems = int(input("How many problems would you like to attempt? "))
    if problems > 0:
        invalidproblems = False
    else:
        print("Invalid number, try again")
        print()

#ask user for width of digit
invaliddigit = True
while invaliddigit:
    digit = int(input("How wide do you want your digits to be? 5-10: "))
    if 5 <= digit and digit <= 10:
        invaliddigit = False
    else:
        print("Invalid width, try again")
        print()

print()

#ask user which character to use for numbers
invalidcharacter = True
while invalidcharacter:
    character = input("What character would you like to use? ")
    if len(character) == 1:
        invalidcharacter = False
    else:
        print("String too long, try again")

#ask for drill mode
invaliddrill = True
while invaliddrill:
    drill = input("Would you like to activate 'drill' mode? yes or no: ")
    if drill == "yes" or drill == "no":
        invaliddrill = False
    else:
        print("Invalid input, try again")

#spacing before questions
print()
print("Here we go!")
print()

#start ocunters
#total correct
counter = 0

#problem counter by type
addition = 0
subtraction = 0
multiplication = 0
division = 0

#correct answer counter by type
correctadd = 0
correctsub = 0
correctmult = 0
correctdiv = 0

#attempts counter by type
addattempts = 0
subattempts = 0
multattempts = 0
divattempts = 0

#for loop for number of questions
for i in range(problems):
    #introduce every question
    print("What is .....")
    print()

    #randomly decide which operator to use
    op = random.randint(0,3)
    #addition
    if op == 0:
        operator = "plus"
        addition += 1
    #subtraction
    elif op == 1:
        operator = "minus"
        subtraction += 1
        
    #times
    elif op == 2:
        operator = "times"
        multiplication += 1

    #divide
    else:
        operator = "divide"
        division += 1

    #get 2 random integers, conditional based on if division or not
    #if division
    if operator == "divide":
        invaliddivision = True
        while invaliddivision:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            
            #if not dividing by 0 and result is an integer
            if num2 != 0 and num1%num2 == 0:
                invaliddivision = False
                
            #keep finding random integers if the numbers don't divide cleanly
    
    #if operation isn't division, just get 2 random integers
    else:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

    #drawa first number
    myfunctions.print_number(num1,digit,character)

    #draw operator and spacing
    print()
    myfunctions.print_operator(operator,digit,character)
    print()

    #draw second number
    myfunctions.print_number(num2,digit,character)

    #processing and counting based on whether drill mode or not
    #drillmode
    if drill == "yes":
        wronganswer = True
        while wronganswer:
            #get user's guess
            useranswer = int(input("= "))
            #check if cororect answer
            if myfunctions.check_answer(num1,num2,useranswer,operator)== True:
                print("Correct!")
                wronganswer = False
            else:
                print("Sorry, that's not correct.")
                #counting attempts
                if operator == "plus":
                    addattempts += 1
                elif operator == "minus":
                    subattempts += 1
                elif operator == "times":
                    multattempts += 1
                elif operator == "divide":
                    divattempts += 1

    #not drill mode            
    else:
        useranswer = int(input("= "))
        #check if correct answer
        if myfunctions.check_answer(num1,num2,useranswer,operator)== True:
            print("Correct!")
            counter += 1
            #counting correct answers
            if operator == "plus":
                correctadd += 1
            elif operator == "minus":
                correctsub += 1
            elif operator == "times":
                correctmult += 1
            elif operator == "divide":
                correctdiv += 1
        else:
            print("Sorry, that's not correct.")

    #check user's guess with check answer function, and tell user if they're correct or not
    print()

#print final statistics
    
#addition
#check for 0 problems of type
if addition > 0:
    #number of additions
    print("Total addition problems presented:",addition)
    #drillmode
    if drill == "yes":
        if addattempts == 0:
            print("#number of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:",addattempts)

    #quiz mode        
    elif drill == "no":
        print("Correct addition problems: ",correctadd," (",format((correctadd/addition)*100,".1f"),"%)",sep="")

else:
    print("No addition problems presented")

print()

#subtraction
if subtraction > 0:
    print("Total subtraction problems presented:",subtraction)
    #drillmode
    if drill == "yes":
        if subattempts == 0:
            print("#number of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:",subattempts)

    #quiz mode        
    elif drill == "no":
        print("Correct addition problems: ",correctsub," (",format((correctsub/subtraction)*100,".1f"),"%)",sep="")

else:
    print("No subtraction problems presented")

print()

#multiplication
if multiplication > 0:
    print("Total multiplication problems presented:",multiplication)
    #drillmode
    if drill == "yes":
        if multattempts == 0:
            print("#number of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:",multattempts)

    #quiz mode        
    elif drill == "no":
        print("Correct multiplication problems: ",correctmult," (",format((correctmult/multiplication)*100,".1f"),"%)",sep="")

else:
    print("No multiplication problems presented")

print()

#division
if division > 0:
    print("Total division problems presented:",division)
    #drillmode
    if drill == "yes":
        if divattempts == 0:
            print("#number of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:",divattempts)

    #quiz mode        
    elif drill == "no":
        print("Correct division problems: ",correctdiv," (",format((correctdiv/division)*100,".1f"),"%)",sep="")

else:
    print("No division problems presented")

print()

#final statement
if drill == "no":
    print("You got",counter,"out of",problems,"correct!")
elif drill == "yes":
    print("Thanks for playing!")
