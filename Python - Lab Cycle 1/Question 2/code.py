import math #importing math module for sqrt

def read(no): #function for reading the sides
    side1 = int(input(f"Enter side 1 of triangle {no}: ")) 
    side2 = int(input(f"Enter side 2 of triangle {no}: "))
    side3 = int(input(f"Enter side 3 of triangle {no}: "))
    print("\n")
    return (area(side1, side2, side3)) #calling the area function and passing the sides


def area(side1, side2, side3):
    sp = (side1+side2+side3)/2 #finding the semi-perimeter
    area = math.sqrt(sp*(sp-side1)*(sp-side2)*(sp-side3)) #calculating area using heron's formula
    return area


area1 = read(1) #function calling and accepting into respective variable
area2 = read(2)
total = area1+area2
print(f"Total area = {total}\n"
      f"Percentage area of triangle 1 = {((area1/total)*100):.4}%\n" #displaying the percentage of the area of each ones
      f"Percentage area of triangle 2 = {((area2/total)*100):.4}%\n")
