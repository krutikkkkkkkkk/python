n = 1
while n >= 0  :
 def add():
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 + num2
    print("{} + {} = {}".format(num1,num2,result))

 def sub():
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 - num2
    print("{} - {} = {}".format(num1,num2,result))

 def mult():
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 * num2
    print("{} x {} = {}".format(num1,num2,result))

 def div():
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 / num2
    print("{} / {} = {}".format(num1,num2,result))

 print("\n1. add \n2. sub\n3. mult\n4. div")

 operation = int(input("\nEnter your choice: "))

 if operation == 1:
    add()
 elif operation == 2:
    sub()
 elif operation == 3:
    mult()
 elif operation == 4: 
    div()
 n = n + 1    
