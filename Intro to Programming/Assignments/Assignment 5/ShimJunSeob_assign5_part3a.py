"""
Assignment #5, Part 3a
Jun Seob Shim
15/10/2020
Intro to Programming Section 012
Prime Number Finder
"""
import math

invalidnum = True

#ask for number to test
while invalidnum:
    num = int(input("Enter a positive number to test: "))

    if num > 0:
        invalidnum = False
    else:
        print("Invalid, try again")

#account for 1 and 2
if num == 1:
    print("1 is technically not a prime number.")
elif num == 2:
    print("2 is a prime number!")
    
#test whether number is prime
else:
    #for determining whether number is prime at the end 
    prime = True

    #divide by integers up to the square root of the number until a divisor is found    
    for i in range(2,math.ceil(num**(1/2))+1):
        #if i is not a factor
        if num % i != 0:
            print(i,"is NOT a divisor of",num,"... continuing")
            
        #if i is a factor
        else:
            print(i,"is a divisor of",num,"... stopping")
            prime = False
            break

    print()
    
    #print if prime or not
    if prime == True:
        print(num,"is a prime number!")
    else:
        print(num,"is not a prime number.")
