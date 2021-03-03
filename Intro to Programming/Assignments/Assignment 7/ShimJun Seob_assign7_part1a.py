"""
Assignment #7, Part 1a
Jun Seob Shim
12/11/2020
Intro to Programming Section 012
Username Validation
"""
#set boolean for while loop to keep asking
invalidusername = True
while invalidusername:
    username = input("Enter a username: ")

    #number of countable characters in username
    uppercase = 0
    lowercase = 0
    digits = 0

    for character in username:
        #uppercase
        if character.isalpha() == True and character == character.upper():
            uppercase += 1

        #lowercase
        elif character.isalpha() == True and character == character.lower():
            lowercase += 1

        #numbers
        elif character.isnumeric() == True:
            digits += 1    

    #check if valid username
    valid = 0
    firstlast = True

    #if any of the criteria are not fulfilled, add 1 to the number 'valid' at the end, check if valid == 0 for a valid username
    #start this one first so this criteria is checked every time (to change the boolean)
    if username[0].isnumeric() == True or username[-1].isnumeric() == True:
        valid += 1
        #determine if false for printing later
        firstlast = False    
    elif username.isalnum() == False:
        valid += 1
    elif len(username) < 8 or 15 < len(username):
        valid += 1
    elif uppercase == 0:
        valid += 1
    elif lowercase == 0:
        valid += 1
    elif digits == 0:
        valid += 1
    
    #print information about username
    print("* Length of username:",len(username))
    print("* All characters are alpha-numeric:",username.isalnum())
    print("* First & last characters are not digits:",firstlast)
    print("* # of uppercase characters in the username:",uppercase)
    print("* # of lowercase characters in the username:",lowercase)
    print("* # of digits in the username:",digits)

    #final check for validity and stopping while loop if valid
    if valid != 0:
        print("Username is invalid, try again")
    else:
        print("Username is valid!")
        invalidusername = False

    #spacing
    print()




    
