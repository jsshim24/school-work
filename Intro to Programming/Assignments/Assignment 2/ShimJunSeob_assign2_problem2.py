"""
Assignment 2, Problem 2
Jun Seob Shim
"""

num1 = int(input("Enter a number between 0 and 999, inclusive: "))
num2 = int(input("Enter another number between 0 and 999, inclusive: "))

#ones
ones1 = num1 % 10
ones2 = num2 % 10

print(format("Sum of ones","15s"),"=",ones1,"+",ones2,"=",ones1+ones2)

num1 = num1 - ones1
num2 = num2 - ones2

#tens
tens1 = int(num1 % 100 / 10)
tens2 = int(num2 % 100 / 10)

print(format("Sum of tens","15s"),"=",tens1,"+",tens2,"=",tens1+tens2)

num1 = num1 - tens1*10
num2 = num2 - tens2*10

#hundreds
hun1 = int(num1 / 100)
hun2 = int(num2 / 100)
print("Sum of hundreds","=",hun1,"+",hun2,"=",hun1+hun2)
