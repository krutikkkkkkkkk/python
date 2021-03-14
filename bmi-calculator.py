weight = int(input("Enter your weight in kg: "))
heightin = float(input("Enter your height in cm: "))

heightin = heightin/100

height = heightin * heightin

bmi = weight/height
print("BMI =", bmi)
if bmi < 18.5:
    print("\nUnderweight")

elif bmi > 18.5 and bmi < 25:
    print("\nNormal")

elif bmi >= 25 and bmi < 30:
    print("\nOverweight")

elif bmi >= 30: 
    print("\nObesity")    
