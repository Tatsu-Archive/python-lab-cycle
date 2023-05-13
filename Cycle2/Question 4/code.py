import random
class Box: # Box class
    length=0
    breadth=0
    height=0
    area=0
    volume=0
    shape="Cube"
    # *args is used to pass variable number of arguments
    def __init__(self,*args): 
        if len(args)==1:
            self.length=args[0]
            self.shape
        elif len(args)==2:
            self.length=args[0]
            self.height=args[1]
            self.shape="Square Prism"
        elif len(args)==3:
            self.length=args[0]
            self.breadth=args[1]
            self.height=args[2]
            self.shape="Rectangular Prism"
    # area and volume methods are defined here
    def area(self):
        if self.breadth==0 and self.height==0:
            self.area=6*self.length**2
        elif self.breadth==0:
            self.area=(2*self.length**2)+(4*self.length*self.height)
        else:
            self.area=2*(self.breadth*self.length+self.height*self.length+self.height*self.breadth)
    def volume(self):
        if self.breadth==0 and self.height==0:
            self.volume=self.length**3
        elif self.breadth==0:
            self.volume=self.length**2*self.height
        else:
            self.volume=self.breadth*self.length*self.height
    # display method is defined here
    def display(self):
        print(f"Area   : {self.area}")
        print(f"Volume : {self.volume}")
        print(f"Ratio  : {self.ratio()}\n")
    # ratio method is defined here
    def ratio(self):
        return self.volume/self.area
# cube, square prism and rectangular prism are generated here
def generate_cube():
    length=random.randint(1,1000)
    return Box(length)
def generate_square_prism():
    length=random.randint(1,1000)
    height=random.randint(1,1000)
    return Box(length,height)
def generate_rectangular_prism():
    length=random.randint(1,1000)
    breadth=random.randint(1,1000)
    height=random.randint(1,1000)
    return Box(length,breadth,height)
# main function
def main():
    num_boxes=int(input("Enter the number of boxes to generate: "))
    boxes=[]
    for i in range(num_boxes):
        if i%3==0:
            box=generate_cube()
        elif i%3==1:
            box=generate_square_prism()
        else:
            box=generate_rectangular_prism()
        print(f"{box.shape} : Dimensions =  [{box.length},{box.breadth},{box.height}]")
        box.area()
        box.volume()
        box.display()
        boxes.append(box)
    
    # max_ratio_box is the box with maximum volume:area ratio
    max_ratio_box=max(boxes,key=lambda box:box.ratio())
    max_ratio=max_ratio_box.ratio()
    if isinstance(max_ratio_box,Box):
        if max_ratio_box.length>0 and max_ratio_box.breadth and max_ratio_box.height==0:
            box_type="Cube"
        elif max_ratio_box.length>0 and max_ratio_box.breadth>0:
            box_type="Rectangular Prism"
        else:
            box_type="Square Prism"
        print(f"Maximum volume:area ratio for {box_type}. Value = {max_ratio}")
    else:
        print("Something went wrong")

main()