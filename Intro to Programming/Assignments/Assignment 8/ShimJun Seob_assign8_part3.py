"""
Assignment #8, Part 3
Jun Seob Shim
19/11/2020
Intro to Programming Section 012
List Functions
"""

def listlen(userlist):
    #set up length counter
    length = 0

    #iterate through list
    for i in userlist:
        length += 1

    return length

def listmax(userlist):
    #set up max value
    biggest = userlist[0]

    #iterate through list
    for i in userlist:
        if i > biggest:
            biggest = i

    return biggest

def listcopy(userlist):
    #create list of zeros
    newlist = [0]*listlen(userlist)

    #iterate through list, setting new list values equal to old list values
    for i in range(listlen(userlist)):
        newlist[i] = userlist[i]

    return newlist
    
def listappend(userlist,data1):
    #create list of zeros that's 1 longer than the supplied list
    newlist = [0]*(listlen(userlist)+1)

    #create a new copy list, with one 0 at the end
    for i in range(listlen(userlist)):
        newlist[i] = userlist[i]

    #set that 0 equal to the supplied data
    newlist[listlen(userlist)] = data1

    return newlist

def listinsert(userlist,location,data1):
    #create list of zeros that's 1 longer than the supplied list
    newlist = [0]*(listlen(userlist)+1)

    for i in range(listlen(newlist)):
        #if the index is the specified location, set to supplied value
        if i == location:
            newlist[i] = data1

        #if before the inserted value, list is same
        elif i < location:
            newlist[i] = userlist[i]

        #if after the inserted value, shift indexing over by 1
        else:
            newlist[i] = userlist[i-1]

    return newlist

def listremove(userlist,data1):
    #create new empty list
    newlist = []

    #iterate through supplied list
    for i in range(listlen(userlist)):

        #if the element is different to what was supplied, add to new list
        if userlist[i] != data1:
            newlist = listappend(newlist,userlist[i])

    return newlist

def listreverse(userlist):
    #create list of zeros
    newlist = [0]*listlen(userlist)

    #iterate through list, setting new list values equal to old list values
    for i in range(listlen(userlist)):
        newlist[i] = userlist[-i-1]

    return newlist
