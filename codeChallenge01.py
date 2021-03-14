"""
WAP to create a basic data collection system using python where:

• It takes username, password and age from input

• It must store atleast 2 user

information taken from input. • After that, it should display the name, total age and avg.

• Atleast 1 of the datastructures should be used.

• You are allowed to use more than one code block
"""

nameOne = input("Enter 1st Name\n")
password = input("Enter password\n")
age1 = input("Enter your age")
print("Name:", nameOne)
print("Password:", password)
print("Age:", age1)
print("_________________________")
nameTwo = input("Enter 2nd Name\n")
password2 = input("Enter password\n")
age2 = input("Enter your age")
print("Name:", nameTwo)
print("Password:", password2)
print("Age:", age2)
print("_________________________")
print("Users:" + nameOne + " and " + nameTwo)
totalAge = int(age1) + int(age2);
average = totalAge /2;
print("Total Age:" , totalAge)
print("Average", average)
