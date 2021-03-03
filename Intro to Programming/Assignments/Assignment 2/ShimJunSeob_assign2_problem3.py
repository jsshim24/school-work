"""
Assignment 2, Problem 3
Jun Seob Shim
"""

#title
print("Minecraft block distance calculator")

print()

#getting user input
x1 = int(input("Block #1 x: "))
y1 = int(input("Block #1 y: "))
z1 = int(input("Block #1 z: "))

x2 = int(input("Block #2 x: "))
y2 = int(input("Block #2 y: "))
z2 = int(input("Block #2 z: "))

print()

#calculating individual distances
xdis = abs(x1-x2)
ydis = abs(y1-y2)
zdis = abs(z1-z2)

#straight line distance
dis = format((xdis**2 + ydis**2 + zdis**2)**0.5,".2f")

#printing with formatting
print("X distance:",xdis)
print("Y distance:",ydis)
print("Z distance:",zdis)
print("Straight line distance:",dis)
