"""
Assignment #3, Problem 3
Jun Seob Shim
9/29/2020
Intro to Programming Section 012
ShimJunSeob_assign3_problem2.py
"""

date = int(input("Enter a date in YYYYMMDD format (i.e. 20200128 for January 28th, 2020): "))

#derive day, month and year
d = int(date % 100)
date = date-d

m = int((date % 10000)/100)
date = date-m*100

y = int(date/10000)

#determine if leap year
leap = False
if y % 4 == 0:
    leap = True

    if y % 100 == 0:
        leap = False

        if y % 400 == 0:
            leap = True

#find if valid date
#by months
if m > 12:
    print("That's not a valid date!")

else:
    #by days
    if m == 1 and d > 31:
        print("That's not a valid date!")
    elif m == 2 and leap == False and d > 28:
        print("That's not a valid date!")
    elif m == 2 and leap == True and d > 29:
        print("That's not a valid date!")
    elif m == 3 and d > 31:
        print("That's not a valid date!")
    elif m == 4 and d > 30:
        print("That's not a valid date!")
    elif m == 5 and d > 31:
        print("That's not a valid date!")
    elif m == 6 and d > 30:
        print("That's not a valid date!")
    elif m == 7 and d > 31:
        print("That's not a valid date!")
    elif m == 8 and d > 31:
        print("That's not a valid date!")
    elif m == 9 and d > 30:
        print("That's not a valid date!")
    elif m == 10 and d > 31:
        print("That's not a valid date!")
    elif m == 11 and d > 30:
        print("That's not a valid date!")
    elif m == 12 and d > 31:
        print("That's not a valid date!")
    else:
        #before and after semester (Semester: Sep 2 2020 ~ Dec 13 2020)
        if y > 2020:
            print("This date is after the semester ends")
        elif y < 2020:
            print("This date is before the semester begins")
        else:
            if m < 9:
                print("This date is before the semester begins")
            elif m == 9 and d < 2:
                print("This date is before the semester begins")
            elif m == 12 and d > 13:
                print("This date is after the semester ends")
            #during semester
            else:
                #September Thursday classes; first on 9/03
                if m == 9 and (d-3) % 7 == 0:
                    print("You have class today")
                    
                #September Tuesday classes; first on 9/08
                elif m == 9 and (d-8) % 7 == 0:
                    print("You have class today")
                    
                #October Thursday classes; first on 10/01
                elif m == 10 and (d-1) % 7 == 0:
                    print("You have class today")
                    
                #October Tuesday Classes; first on 10/06
                elif m == 10 and (d-6) % 7 == 0:
                    print("You have class today")
                    
                #November Thanksgiving exception, no class
                elif m == 11 and d == 26:
                    print("You do not have class today")

                #November Tuesday Classes; first on 11/03
                elif m == 11 and (d-3) % 7 == 0:
                    print("You have class today")

                #November Thursday Classes; first on 11/05 
                elif m == 11 and (d-5) % 7 == 0:
                    print("You have class today")

                #December Tuesday Classes; first on 12/01
                elif m == 12 and (d-1) % 7 == 0:
                    print("You have class today")

                #December Thursday Classes; first on 12/03
                elif m == 12 and (d-3) % 7 == 0:
                    print("You have class today")
                    
                else:
                    print("You do not have class today")    







        

