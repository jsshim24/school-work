
"""
Assignment #1, Problem 2
Jun Seob Shim
"""

print()

name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")

print()

print("Here are your names in every possible order:")
print("--------------------------------------------")

print()

#name1, name2, name3
print("1. ", end="")
print(name1, name2, name3, sep=", ")
print()

#name1, name3, name2
print("2. ", end="")
print("", name1, " ", name3, " ", name2, " ", sep="*")
print()

#name2, name1, name3
print("3. ", end="")
print(name2, name1, name3, sep="-")
print()

#name2, name3, name1
print("4. ", end="")
print(name2)
print(name3)
print(name1)
print()

#name3, name2, name1
print("5. ", end="")
print(name3)
print("   " + name2)
print("   " + name1)
print()

#name3, name1, name2
print("6. ", end="")
print(name3)
print("---" + name1)
print("---" + name2)
