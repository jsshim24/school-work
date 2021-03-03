"""
Assignment #5, Part 2
Jun Seob Shim
15/10/2020
Intro to Programming Section 012
Dynamic Gradebook
"""

invalidstudents = True

#ask for number of students
while invalidstudents:
    students = int(input("How many students are in your class? "))

    if students > 0:
        invalidstudents = False
    else:
        print("Invalid # of students, try again.")
        print()

invalidtests = True

#ask for number of tests
while invalidtests:
    tests = int(input("How many tests in this class? "))

    if tests > 0:
        print()
        print("Here we go!")
        print()
        invalidtests = False
    else:
        print("Invalid # of tests, try again.")

#intitialize combinedtotal variable
combinedtotal = 0


#ask for test scores for all students
for i in range(students):
    print("*"*4," Student #",i+1,"","*"*4,sep="")

    #initialize totalscore variable
    totalscore = 0   
    
    #ask for score for all tests
    for j in range(tests):
        invalidscore = True

        #check for invalid test scores
        while invalidscore:
            print("Enter score for test #",j+1,sep="",end="")
            score = int(input(": "))
            
            if 0 <= score <= 100:
                invalidscore = False
            else: 
                print("Invalid score, try again")

        #keep track of sum of tests for this student
        totalscore += score

    #keep track of sum of all scores    
    combinedtotal += totalscore

    #print average score for each student
    print("Average score for student #",i+1," is ",format(totalscore/tests,".2f"),sep="")
    print()

#print overall average
print("Average score for all students is:",format(combinedtotal/(students*tests),".2f"))


