number = str(input("Enter a number: "))
numberint = list(number)
numberlist = "1234567890"
numberlist = list(numberlist)

i = 0;
temp = 0;
for i in range(number.__len__()):
    if  numberint[i] not in numberlist:
        print("Invalid Input, Enter a number")
        exit()
    else:
        temp += int(numberint[i])**3
        
if(temp != int(number)):
    print("Its not an Armstrong Number")  
             
else:
    print("Its an Armstrong Number")
             
    