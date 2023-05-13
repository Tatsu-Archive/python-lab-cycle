
class _3D_Shapes: # Abstract class
    def print_Volume(self):
        print("Volume: ", self.volume)

    def print_Area(self):
        print("Area: ", self.area)


class Cylinder(_3D_Shapes): # Cylinder class
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def calculate_Volume(self): # Volume of cylinder
        self.volume = 3.14 * self.radius * self.radius * self.height
        _3D_Shapes.print_Volume(self)
     
    def calculate_Area(self): # Surface area of cylinder
        self.area = 2 * 3.14 * self.radius * (self.radius + self.height)
        _3D_Shapes.print_Area(self)
    

class Sphere(_3D_Shapes): # Sphere class
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_Volume(self): # Volume of sphere
        self.volume = (4/3) * 3.14 * self.radius * self.radius * self.radius
        _3D_Shapes.print_Volume(self)
    
    def calculate_Area(self): # Surface area of sphere
        self.area = 4 * 3.14 * self.radius * self.radius
        _3D_Shapes.print_Area(self)

    
def main(): # main function
    print("Cylinder")
    cylinr= int(input("Enter the radius: "))
    cylinh= int(input("Enter the height: "))
    cylin = Cylinder(cylinr, cylinh)
    cylin.calculate_Volume() 
    cylin.calculate_Area()

    print()
    print("Sphere")
    sphr = int(input("Enter the radius: "))
    sph = Sphere(sphr)
    sph.calculate_Volume()
    sph.calculate_Area()


main() # main function call
