# Python code to find the entered year is a leap year or not
year = int(input("Enter any Year: \n"))

leapYear = year%4

if leapYear == 0 :
    print("Its a Leap Year")
else:
    print("Its not a Leap Year")    
