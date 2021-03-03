"""
Assignment #4, Part 3
Jun Seob Shim
8/10/2020
Intro to Programming Section 012
Modern Art Monte Carlo Simulation
"""
import time as t
import random as r
import turtle

invalidthrows = True

while invalidthrows:
    throws = int(input("Number of throws: "))
    if throws > 0:
        invalidthrows = False
    else:
        print("Invalid, try again!")

invalidturtle = True

while invalidturtle:
    turtles = input("Would you like to draw your results using turtle graphics? (yes/no): ")
    if turtles == "yes":
        invalidturtle = False
    elif turtles == "no":
        invalidturtle = False
    else:
        print("Invalid, try again")

#initialize counters for colors
red = 0
green = 0
blue = 0
grey = 0
lgrey = 0

#setup turtle
if turtles == "yes":
    turtle.setup(800,500)
    turtle.tracer(0)
    turtle.hideturtle()

#take time
timebefore = t.time()

#for loop
for counter in range(throws):
    x = r.uniform(0,800)
    y = r.uniform(0,500)

    #prepare to draw
    if turtles == "yes":
        turtle.penup()

    #red regtancle
    if 350 <= x <= 450 and 300 <= y <= 450:
        red += 1
        turtle.pencolor("#ff0405")
    #full green rectangle
    if 550 <= x <= 750 and 50 <= y <= 450:
        green += 1
        turtle.pencolor("#00ff00")
    #account for holes in green rectangle
    if 600 <= x <= 700 and 100 <= y <= 200:
        green -= 1
        turtle.pencolor("white")
    if 600 <= x <= 650 and 250 <= y <= 300:
        green -= 1
        turtle.pencolor("white")
    if 650 <= x <= 700 and 350 <= y <= 400:
        green -= 1
        turtle.pencolor("white")
    #blue circle (center: 400, 150)
    if ((400-x)**2 + (150-y)**2)**(1/2) <= 100:
        blue += 1
        turtle.pencolor("#1200ff")
    #large grey circle (center: 150,300)
    if ((150-x)**2 + (300-y)**2)**(1/2) <= 100:
        grey += 1
        turtle.pencolor("#333333")
    #small grey circle (center: 150, 200)
    if ((150-x)**2 + (200-y)**2)**(1/2) <= 50:
        grey +=1
        turtle.pencolor("#333333")
    #-2 for the 2 grey counts, light grey area
    if ((150-x)**2 + (300-y)**2)**(1/2) <= 100 and ((150-x)**2 + (200-y)**2)**(1/2) <= 50:
        grey -= 2
        lgrey += 1
        turtle.pencolor("#cccccc")
    
    if turtles == "yes":
        turtle.goto(x-400-5,250-y+5)
        turtle.pendown()
        turtle.goto(x-400+5,250-y-5)
        turtle.penup
        turtle.pencolor("white")

#post loop debrief
#draw memory to screen
turtle.update()

#calculate time taken
timeafter = t.time()
print()
print("Total time elapsed:",format(timeafter-timebefore,".2f"),"seconds")

#calculate misses
misses = throws-(red+blue+green+grey+lgrey)
#format numbers with commas
sred = format(red,",d")
sblue = format(blue,",d")
sgreen = format(green,",d")
sgrey = format(grey,",d")
slgrey = format(lgrey,",d")
smisses = format(misses,",d")

#format and print strings
print(format("Red:","16s"),format(sred,">6s")," (",format((red/throws)*100,".2f"),"%)",sep="")
print(format("Blue:","16s"),format(sblue,">6s")," (",format((blue/throws)*100,".2f"),"%)",sep="")
print(format("Green:","16s"),format(sgreen,">6s")," (",format((green/throws)*100,".2f"),"%)",sep="")
print(format("Dark Grey:","16s"),format(sgrey,">6s")," (",format((grey/throws)*100,".2f"),"%)",sep="")
print(format("Light Grey:","16s"),format(slgrey,">6s")," (",format((lgrey/throws)*100,".2f"),"%)",sep="")
print(format("Misses:","16s"),format(smisses,">6s")," (",format((misses/throws)*100,".2f"),"%)",sep="")
