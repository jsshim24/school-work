"""
Assignment #7, Part 3
Jun Seob Shim
12/11/2020
Intro to Programming Section 012
Middle Squares Pseudorandom Number Generator
"""
import math

#start while loop to get seed number
invalidinput = True
while invalidinput:
    #get seed number from user
    seed = input("Enter a six digit seed: ")

    #if seed number is valid
    if len(seed) == 6 and seed.isnumeric()== True:
        #stop while loop
        invalidinput = False

        #get low and high bounds from user
        invalidbounds = True
        while invalidbounds:
            lowbound = input("Enter lowest possible random integer: ")
            highbound = input("Enter highest possible random integer: ")

            if lowbound.isnumeric() == True and highbound.isnumeric() == True:
                #stop while loop
                invalidbounds = False

                #spacing
                print()

                invalidnumbers = True
                while invalidnumbers:
                    stringnumbers = input("How many random numbers do you want to generate? ")
                    
                    if stringnumbers.isnumeric() == True:
                        
                        #spacing
                        print()
                        
                        invalidnumbers = False
                        #convert string inputs into integers for use
                        low = int(lowbound)
                        high = int(highbound)

                        #convert string numbers into int for use
                        numbers = int(stringnumbers)

                        #print seed
                        print("Seed value:",seed)
                        
                        for i in range(numbers):
                            #calculations
                            #square and print
                            squared = int(seed)**2
                            print("Square of seed:",squared)

                            #convert int to string
                            strsquared = str(squared)

                            #get middle 6 digits of square and print
                            #if the square is 11 digits long
                            if len(strsquared) == 11:
                                middle = strsquared[2:8]

                            #if the square is 12 digits long
                            else:
                                middle = strsquared[3:9]

                            #print middle
                            print("Middle 6 digits of square:",middle)

                            #set new seed for next iteration
                            seed = middle

                            #get percentage and print
                            percentage = int(middle)/999999
                            print("Percentage =",middle,"/ 999999 =",percentage)

                            #scale to bounds
                            print("Scaling up to a number between",low,"and",high)

                            #calculate actual random number
                            random = (high-low)*percentage + low

                            #print calculation of random number
                            print(high,"-",low,"*",percentage,"+",low,"=",random)
                            
                            #print random number converted to integer
                            print("Converted to an integer:",math.floor(random))

                            #spacing
                            print()

                    else:
                        print("Invalid, try again")
                        print()

            else:
                print("Invalid low/high values, please try again.")
                print()

    #if invalidinput
    else:
        print("Invalid seed, try again.")
        print()
    
