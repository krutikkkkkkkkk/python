num = int(input("Enter any number\n"))
factorial = 1
if num < 0:
    print("Sorry, factorial doesn't exist for negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num):
        factorial += factorial*i
    print("The factorial of {} is {}".format(num,factorial))
