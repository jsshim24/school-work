"""
Assignment #8, Part 1
Jun Seob Shim
19/11/2020
Intro to Programming Section 012
Sieve of Eratosthenes
"""
#get numbers to test from user
invalidnum = True
while invalidnum:
    usernum = input("Enter a positive integer greater than or equal to 10: ")
    n = int(usernum)
    if n >= 10:
        invalidnum = False
    else:
        print("Invalid input, try again.")
        print()

#creating list
primelist = ["P"]*(n+1)

#editing that list
for i in range(len(primelist)):
    #if number is 0 or 1, set to not prime
    if i <= 1:
        primelist[i] = "N"

    #if number is 2 or greater, and has multiples in the set    
    elif i >= 2 and i*2 <= n:
        #if the value is prime
        if primelist[i] == "P":
            #for multiples of the value, setto not prime
            for j in range(2,n//i+1):
                primelist[i*j] = "N"
        else:
            #if the number isn't prime, skip to next number
            continue

#printing the list orderly
#get length of the largest number (number entered by user) and add 1 for spacing
length = len(usernum)+1

#establish counter (count every 10)
counter = 1

#run through the list
for k in range(len(primelist)):
    #print if prime
    if primelist[k] == "P":
        print(format(k,f'<{length}'),end=" ")
        if counter%10 == 0:
            print()
        counter += 1
        
