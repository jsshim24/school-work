"""
Assignment #11, Part 3
Jun Seob Shim
10/12/2020
Intro to Programming Section 012
Smartphone
"""
#define smartphone class
class Smartphone:

    #constructor
    def __init__(self,capacity,name):

        #initial constructor variables
        self.space = capacity
        self.phonename = name

        #other variables for processing
        self.spacetaken = 0
        self.spaceleft = self.space-self.spacetaken
        self.apps = []
        self.appspace = []

        #print success
        print("Smartphone created!")

        #call report method
        self.report()

    #report method
    def report(self):

        #print attributes and information
        print("Name: "+self.phonename)
        print("Capacity: "+str(self.spacetaken)+" out of "+str(self.space)+" GB")
        print("Available space: "+str(self.spaceleft))
        print("Apps installed: "+str(len(self.apps)))

        #for printing apps, print in alphabetical order
        self.sortedapps = self.apps.copy()
        self.sortedapps.sort()
        self.sortedappspace = []

        #create new list of sorted appspace with correct space values for sorted apps
        for i in range(len(self.apps)):
            position = self.apps.index(self.sortedapps[i])
            self.sortedappspace.append(self.appspace[position])

        #if there are apps installed, print detailed info
        if len(self.apps) > 0:
            for i in range(len(self.apps)):
                print("* "+self.sortedapps[i]+" is using "+str(self.sortedappspace[i])+" GB")

        #print for spacing
        print()

    #add app
    def add_app(self,appname,appsize):

        #if app isn't on phone already
        if (appname in self.apps) == False:

            #if there is space for the app
            if self.spaceleft > appsize:

                #add app and space to corresponsing lists
                self.apps.append(appname)
                self.appspace.append(appsize)

                #adjust space values
                self.spacetaken += appsize
                self.spaceleft -= appsize

            #if no space
            else:
                print("Cannot install app, no available space")

        #if app is already installed
        else:
            print("Cannot install app, already installed")

    #remove app
    def remove_app(self,appname):

        #if app is on phone
        if (appname in self.apps) == True:

            #find where the app is on list
            index = self.apps.index(appname)

            #adjust space values before deleting
            self.spacetaken -= self.appspace[index]
            self.spaceleft += self.appspace[index]

            #delete app and corresponding space value            
            del self.apps[index]
            del self.appspace[index]     

        #if app isn't on phone
        else:
            print("Cannot remove app, not installed")

    #check if phone has app (not called during main program)
    def has_app(self,appname):
        return(appname in self.apps)

    #check how much space left (not called during main program)
    def get_available_space(self):
        return(self.spaceleft)

#main program

#set up while loop
invalidsize = True

while invalidsize:

    #get integer size from user
    size = int(input("Size of your new smartphone (32, 64 or 128 GB): "))

    #if valid size
    if size == 32 or size == 64 or size == 128:

        #end while loop
        invalidsize = False

        #get name of phone from user
        name = input("Smartphone name: ")

        #create new phone with supplied information
        newphone = Smartphone(size,name)

        #set up while loop for phone functions
        notquit = True
        
        while notquit:
            mode = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")

            #if report mode
            if mode == "r":
                newphone.report()

            #if add mode
            elif mode == "a":

                #get properties for app to add
                appname = input("App name to add: ")
                appsize = int(input("App size in GB: "))
                
                newphone.add_app(appname,appsize)

            #if remove mode
            elif mode == "e":

                #get appname to remove
                appname = input("App name to remove: ")

                newphone.remove_app(appname)

            #if quit mode
            else:
                print("Goodbye!")

                #end while loop
                notquit = False

            #after every call of a phone function, print for spacing
            print()            

    #if invalid phone space size
    else:
        print("Invalid size, try again")
