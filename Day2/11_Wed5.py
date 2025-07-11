# finding number of the digit
num = int(input("enter the number up to 5 digit:"))

if num >= 0 and num <=9:
    print("the number is single digit")
    
elif num >= 10 and num <= 99:
    print("the number is double digit")    

elif num >= 100 and num <= 999:
    print("the number is triple digit") 

elif num >= 1000 and num <= 9999:
    print("the number is four digit") 

elif num >= 10000 and num <= 99999:
    print("the number is five digit")   

else:
    print("invalid input")      
            