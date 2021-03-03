"""
Assignment #5, Part 3b
Jun Seob Shim
15/10/2020
Intro to Programming Section 012
Find all prime numbers between 1 and 1000
"""
import math

#start with 2
print("2 is a prime number!")
    
#up until 999  
for a in range(2,1000):
    
    #for determining whether number is prime at the end
    prime = True

    #test whether number is prime
    for i in range(2,math.ceil(a**(1/2))+1):
        #if i is not a factor
        if a%i == 0:
            prime = False
            break

    #print if prime
    if prime == True:
        print(a,"is a prime number!")
