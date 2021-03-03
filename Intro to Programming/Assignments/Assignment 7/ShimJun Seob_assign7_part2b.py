"""
Assignment #7, Part 2b
Jun Seob Shim
12/11/2020
Intro to Programming Section 012
Encoding/decoding Functions
"""
import ShimJunSeob_assign7_part2a as code

invalidselection = True
#select program mode
while invalidselection:
    #get mode from user
    mode = input("(e)ncode, (d)ecode, or (q)uit: ")

    #check which mode
    #if the mode is encode or decode
    if mode == "e" or mode == "d":
        num = int(input("Enter a number between 1 and 5: "))

        #if the supplied number isn't valid 
        if num >= 1 and num <= 5:
            #encoding
            if mode == "e":
                word = input("Enter a phrase to encode: ")
                coded = code.add_letters(word,num)
                print("Your encoded string is:",code.shift_characters(coded,num))

            #decoding
            else:
                word = input("Enter a phrase to decode: ")
                decoded = code.remove_letters(word,num)
                print("Your decoded string is:",code.shift_characters(decoded,-(num)))

            #spacing
            print()

        #if the supplied number isn't valid
        else:
            print("Invalid input, try again.")

    #exit while loop if q mode
    elif mode == "q":
        break

    #if the chosen mode isn't valid
    else:
        print("Invalid input, try again.")
