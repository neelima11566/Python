# Area Calculator
print("Area Calcultor")
print("""press 1 to get area of square
      press 2 to get area of rectangle
      press 3 to get area of circle
      press 4 to get area of triangle""")

choice = int(input("enter a number between 1-4:"))

if choice == 1:
    side = float(input("enter the side of the square:"))
    area = side * 2
    print("Area of the square:", area)

elif choice == 2:
     lenght = float(input("enter the value of lenght: "))
     breadth = float(input("enter the value of breadth: "))
     area = lenght * breadth
     print("Area of the rectangle:", area)
     
elif  choice == 3:
     radius = float(input("enter the value of radius:"))
     area = (3.14) * (radius ** 2)
     print("Area of the circle:", area)

elif  choice == 4:
     base = float(input("enter the value of base:"))
     heigth = float(input("enter the value of height:4"))
     area = 0.5 * heigth * base
     print("Area of the triangle:", area)     
     
else:
    print("Wronge input")     
         