# logical operator
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
num3 = float(input("enter third number"))

if (num1 > 0) and (num2 > 0) and (num3 > 0):
    print("all number are greater than zero")
    
elif (num1 % 2 == 0) or (num2 % 2 == 0):
    print("even number")    
else:
    print("invalid input")    
    
age = 15
if not age >= 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")