"""
Assignment #7, Part 4
Jun Seob Shim
12/11/2020
Intro to Programming Section 012
String Functions
"""
def string_length(word):
    #length counter
    length = 0

    #iterate through string
    for character in word:
        #add to length
        length += 1

    return length

def string_isalpha(word):
    #establish isalpha as false
    isalpha = False

    #iterate through string
    for character in word:
        #if either lower or uppercase alpha, keep going and saying true
        if ord(character)>= 65 and ord(character) <= 90: 
            isalpha = True
        elif ord(character) >= 97 and ord(character) <= 122:
            isalpha = True

        #if there is a non alphabetic character, end immediately and declare not alpha
        else:
            isalpha = False
            break
            
    return isalpha

def string_isupper(word):
    #start with not upper
    isupper = False

    #iterate through string
    for character in word:
        #set to true if uppercase letters
        if ord(character) >= 65 and ord(character) <= 90: 
            isupper = True

        #if non capital letter found, immediately declare not uppercase
        else:
            isupper = False
            break

    return isupper
        
def string_isdigit(word):
    #start with not digit
    isdigit = False

    for character in word:
        #set to true if digit
        if ord(character) >= 48 and ord(character) <= 57:
            isdigit = True

        #if non digit found, immediately declare not digit
        else:
            isdigit = False
            break

    return isdigit

def string_swapcase(word):
    #make new empty string to add to
    newword = ""

    #iterate through word
    for character in word:
        #if uppercase
        if ord(character)>= 65 and ord(character) <= 90: 
            newword += chr(ord(character) + 32)

        #if lowercase
        elif ord(character) >= 97 and ord(character) <= 122:
            newword += chr(ord(character) - 32)

        #if not alpha, just leave as is
        else:
            newword += character

    return newword


def string_lower(word):
    #creat empty string to add to
    newword = ""

    #iterate through word
    for character in word:
        #if uppercase
        if ord(character)>= 65 and ord(character) <= 90:
            newword += chr(ord(character) + 32)

        #if not uppercase, just leave as is
        else:
            newword += character

    return newword
