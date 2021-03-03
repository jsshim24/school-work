"""
Assignment #10
Jun Seob Shim
8/12/2020
Intro to Programming Section 012
Thesaurus
"""
#import random module
import random

#define thesaurus
#start counter for how many words there are
wordcounter = 0
#open file for reading
thesaurus_file = open("python_asg10_Roget_Thesaurus.txt","r")

"""
the thesaurus file is messed up somehow and a lot of the synonyms are just wrong (eg. synonyms for "happy" are agreement,
cheerfulness,elegance,occasion,pleasure)which obviously doesn't make any sense. should a identically named, valid thesaurus
file be supplied, the program should work as intended
"""

#create empty dictionary to add to
thesaurus = {}

#reading and processing data from file
alldata = thesaurus_file.read()

#split into list by lines
giantlist = alldata.split("\n")

#for each word and its synonyms
for i in range(len(giantlist)):
    #split each line into a list by words
    wordlist = giantlist[i].split(",")
    #count number of words in thesaurus
    wordcounter += len(wordlist)

    #conditions based on how many synonyms
    if len(wordlist) > 2:
        synonyms = wordlist[1:len(wordlist)-1]
    elif len(wordlist) == 2:
        synonyms = [wordlist[1]]
    else:
        synonyms = []

    #add to dictionary (thesaurus)
    thesaurus[wordlist[0]] = synonyms

#close file
thesaurus_file.close()

#print prelim data
print("Total words in thesaurus: ",wordcounter)
print()

#ask user for input chance
chance = float(input("Enter a % chance to change a word: "))

#open lyrics file
baby_file = open("bieber_baby.txt","r")

#take out into long string, and close
phrase = baby_file.read()
baby_file.close()

#set up new phrase to add to (remove punctuation)
newphrase = ""

#iterate over supplied phrase, and add to empty string
for i in phrase:
    if i.isalpha() == True or i.isspace() == True:
        newphrase += i.lower()

#split new string into a list (by words)
phraselist = newphrase.split(" ")

#create new empty string to put final result in
applied = ""

#iterate over thesaurus
for key, value in thesaurus.items():
    #if the key is in the list of words
    if (key in phraselist) == True:
        #iterate over the words in the list
        for i in range(len(phraselist)):
            #if the element equals a key
            percentage = random.random()
            if phraselist[i] == key and percentage < chance:
                #pick a random value and replace
                if len(value)== 0:
                    continue
                else:
                    r = random.randint(0,len(value)-1)
                    phraselist[i] = value[r-1].upper()

#add the list back to the empty string with spaces
for i in range(len(phraselist)):
    applied += phraselist[i] + " "

#print final transformed string
print(applied)
