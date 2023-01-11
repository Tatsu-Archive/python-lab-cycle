import math


def read(no):
    side1 = int(input(f"Enter side 1 of triangle {no}: "))
    side2 = int(input(f"Enter side 2 of triangle {no}: "))
    side3 = int(input(f"Enter side 3 of triangle {no}: "))
    print("\n")
    return (area(side1, side2, side3))


def area(side1, side2, side3):
    sp = (side1+side2+side3)/2
    area = math.sqrt(sp*(sp-side1)*(sp-side2)*(sp-side3))
    return area


area1 = read(1)
area2 = read(2)
total = area1+area2
print(f"Total area = {total}\n"
      f"Percentage area of triangle 1 = {((area1/total)*100):.4}%\n"
      f"Percentage area of triangle 2 = {((area2/total)*100):.4}%\n")
