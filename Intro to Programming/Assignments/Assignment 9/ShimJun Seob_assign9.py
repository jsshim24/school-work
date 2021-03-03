"""
Assignment #9
Jun Seob Shim
1/12/2020
Intro to Programming Section 012
Exam Gradebook
"""
import statistics

#set up while loop
invalidfilename = True

while invalidfilename:

    #get filename from user, and add file extensiono
    file = input("Enter a class file to grade (ie. class1 for class1.txt): ")
    filename = file + ".txt"
    #try to open file
    try:
        #open with read access
        scores = open(filename,"r")

    #if file is not found
    except:
        print("File cannot be found.")
        print()

        #skips below if filename is invalid
        continue

    #if filename is valid, end while loop and print success
    invalidfilename = False
    print("Successfully opened",filename)

#establish answerkey
answerkey = ["B","A","D","D","C","B","D","A","C","C","D","B","A","B","A","C","B","D","A","C","A","A","B","D","D"]

#get all data
allanswers = scores.read()

#split into each student's data
splitdata = allanswers.split("\n")

#invalidlines
invalidstudent = 0

#create list of student scores
studentscores = []

#generate results file
resultsname = file + "_grades.txt"
results = open(resultsname,"w")

#for each student
for i in range(len(splitdata)):
    
    #score tracking
    score = 0

    #get a separate string for the specific student
    student = splitdata[i]

    #split into list
    splitstudent = student.split(",")

    #if invalid list
    if len(splitstudent) != 26:
        #count invalid entries
        invalidstudent += 1

        #skip below code
        continue
    
    #scoring test
    for i in range(len(splitstudent)-1):
        if splitstudent[i+1] == answerkey[i]:
            score += 4
        elif splitstudent[i+1] == "":
            score += 0
        else:
            score -= 1

    #add student's score to list of scores
    studentscores.append(score)

    #write student ID to results document
    results.write(splitstudent[0])
    #also write student's score to results document (with formatting)
    results.write(","+format(score,".2f")+"\n")

#close results file
results.close()

#print summary
print()
print("Grade Summary:")
print("Total students:", len(studentscores))
print("Unusable lines in the file:", invalidstudent)
print("Highest score:",max(studentscores))
print("Lowest score:",min(studentscores))
mean = sum(studentscores)/len(studentscores)
print("Mean score:",format(mean,".2f"))

#calculate median
studentscores.sort()

length = len(studentscores)
if length % 2 == 0:
    middle = length//2
    median = (studentscores[middle-1]+studentscores[middle])/2
else:
    middle = length/2
    median = studentscores[int(middle-0.5)]

print("Median score:",median)

#calculate mode
#establish 2 new empty lists
uniquescores = []
frequency = []


for i in studentscores:
    if (i in uniquescores) == False:
        uniquescores.append(i)
        frequency.append(1)

    else:
        frequency[uniquescores.index(i)] += 1

#establish empty string and max frequency
mode = ""
frequent = max(frequency)

#iterate through frequency, and find all maxes
for i in range(len(frequency)):

    #if frequency is equal to the max frequency, add to 'mode'
    if frequency[i] == frequent:
        mode += str(uniquescores[i]) + " "

#print
print("Mode:",mode)

#calculate range
print("Range:",studentscores[-1]-studentscores[0])

#curve
invalidcurve = True
while invalidcurve:
    curve = input("Would you like to curve the exam? 'y' or 'n': ")
    if curve == "y":
        invalidcurve = False
        
        invalidmean = True
        while invalidmean:
            curvemean = float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
            if curvemean > mean:
                invalidmean = False
                #overwrite existing file
                results = open(resultsname,"w")

                #for each student
                for i in range(len(splitdata)):
                    
                    #score tracking
                    score = 0

                    #get a separate string for the specific student
                    student = splitdata[i]

                    #split into list
                    splitstudent = student.split(",")

                    #if invalid list
                    if len(splitstudent) != 26:
                        #count invalid entries
                        invalidstudent += 1

                        #skip below code
                        continue
                    
                    #scoring test
                    for i in range(len(splitstudent)-1):
                        if splitstudent[i+1] == answerkey[i]:
                            score += 4
                        elif splitstudent[i+1] == "":
                            score += 0
                        else:
                            score -= 1

                    #add student's score to list of scores
                    studentscores.append(score)

                    #write student ID to results document
                    results.write(splitstudent[0])
                    #also write student's score to results document (with formatting)
                    results.write(","+format(score,".2f"))
                    #also write student's curved score
                    results.write(","+format(score+(curvemean-mean),".2f")+"\n")

                #print success
                print("Done! Check your grade file!")
                
            else:
                print("Invalid curve, try again.")
                print()

    elif curve == "n":
        invalidcurve = False
    else:
        print("Invalid input, try again")
        print()

#close files
scores.close()
results.close()
    
