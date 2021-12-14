import math
""" class Apple:
    def __init__(self,c,w,d):
        self.color = c
        self.weight = w
        self.diameter = d
        print("Created!")

app1 = Apple("Red", 100, 80)
print(app1.color)
print(app1.weight) """

""" class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * math.pi

cir1 = Circle(5.0)
print(cir1.area()) """

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5

current_b = float(input())
current_h = float(input())
cir1 = Triangle(current_b,current_h)
print(cir1.area())