"""
Assignment #5, Part 3c
Jun Seob Shim
15/10/2020
Intro to Programming Section 012
Tabular Formatting

Sources:
Using variables in the format function: https://stackoverflow.com/questions/32413109/using-variables-in-the-format-function-in-python
"""
import math

invalidbounds = True

#ask user for bounds
while invalidbounds:
    start = int(input("Start number: "))
    end = int(input("End number: "))

    if start > 0 and end > 0:
        #if both bounds are positive, and end bound is greater than the start bound
        if end > start:
            invalidbounds = False
        #if end bounds is smaller than the start bound
        else:
            print("End number must be greater than start number")
            print()
    #if one or more bounds are negative
    else:
        print("Start and end must be positive")
        print()

#find length of largest number (end bound)
length = len(str(end))

#number counter
counter = 1

#test for primes within range specified
for a in range(start,end+1):
    
    #for determining whether number is prime at the end
    prime = True

    #skip when a = 1 if 1 is within range
    if a == 1:
        continue

    #print 2 and skip when a = 2 if 2 is within range
    elif a == 2:
        #format string to length of end bound
        print(format(a, f'>{length}'),end=" ")
        counter += 1
        continue
    
    #if a is not 1 or 2, test whether number is prime
    else:
        for i in range(2,math.ceil(a**(1/2))+1):
            #if i is not a factor
            if a%i == 0:
                prime = False
                break

    #print if prime
    if prime == True:
        #format string to length of end bound
        print(format(a, f'>{length}'),end=" ")
        if counter % 10 == 0:
            print()
        counter += 1
        
