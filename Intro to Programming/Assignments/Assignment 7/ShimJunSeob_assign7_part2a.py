"""
Assignment #7, Part 2a
Jun Seob Shim
12/11/2020
Intro to Programming Section 012
Encoding/decoding Functions
"""
import random

#add letters
def add_letters(word,num):
    #create empty string for new word
    newword = ""

    #iterate through string
    for character in word:
        
        #generate num letters to add
        add = ""
        #iterate through num
        for i in range(num):
            #choose between capital or lowercase
            num1 = random.randint(0,1)
            #capital
            if num1 == 0:
                add += chr(random.randint(65,90))
            #lowercase
            else:
                add += chr(random.randint(97,122))

        newword += character + add

    return newword

#remove letters
def remove_letters(word,num):
    newword = ""
    for i in range(len(word)):
        if i%(num+1) == 0:
            newword += word[i]

    return newword

#shift characters
def shift_characters(word,num):
    newword = ""
    for character in word:
        newword += chr(ord(character)+num)

    return newword
