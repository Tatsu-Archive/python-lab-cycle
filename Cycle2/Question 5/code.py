import math

class ThreeDShapes:
    def __init__(self, *args):
        self.radius = args[0]
        self.height = args[1]
        self.area = 0
        self.volume = 0

    def calcArea(self):
        pass

    def calcVolume(self):
        pass

    def printVolume(self):
        print(f'Volume: {self.volume}')

    def printArea(self):
        print(f'Area: {self.area}')

class Cylinder(ThreeDShapes):
    def calcArea(self):
        self.area = 2 * math.pi * self.radius * (self.radius + self.height)

    def calcVolume(self):
        self.volume = math.pi * self.radius * self.radius * self.height

class Sphere(ThreeDShapes):
    def calcArea(self):
        self.area = 4 * math.pi * self.radius * self.radius

    def calcVolume(self):
        self.volume = 4 / 3 * math.pi * self.radius * self.radius * self.radius

radius = int(input('Enter the radius: '))
height = int(input('Enter the height: '))
cylinder = Cylinder(radius, height)
cylinder.calcArea()
cylinder.calcVolume()
cylinder.printArea()
cylinder.printVolume()


