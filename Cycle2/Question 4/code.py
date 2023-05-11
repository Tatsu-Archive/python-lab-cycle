import random

class Box:
    def __init__(self, *args):
        self.length = args[0]
        self.breadth = args[1]
        self.height = args[2]
        self.area = 0
        self.volume = 0

    def calcArea(self):
        self.area = 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)

    def calcVolume(self):
        self.volume = self.length * self.breadth * self.height

    def __str__(self):
        return f'Length: {self.length}\nBreadth: {self.breadth}\nHeight: {self.height}\nArea: {self.area}\nVolume: {self.volume}\n'

n = int(input('Enter the number of boxes: '))
boxes = []
for i in range(n):
    boxes.append(Box(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)))
    boxes[i].calcArea()
    boxes[i].calcVolume()
maxVol = 0
for i in range(n):
    if boxes[i].volume > boxes[maxVol].volume:
        maxVol = i
print(f'Box with maximum volume: {boxes[maxVol]}')
print(f'Area:Volume ratio of box with maximum volume: {boxes[maxVol].area / boxes[maxVol].volume}')
