# nested if
num = int(input("enter number"))

if num % 2 == 0:
    print("number is divisible by 2")
    
    if num % 5 == 0:
        print("number is divisible by 5")
    else:
        print("number is not divisible by 5")
else:
    print("number is not divisible by 2")            
    