class Shape:
    def __init__(self):
        pass
    
    def what_am_i(self):
        print("I am a Shape")

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square(Shape):
    def __init__(self,s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
    
    def change_size(self,defferential):
        self.s1 += defferential

rec1 = Rectangle(25,20)
squ1 = Square(20)

rec1.what_am_i()
squ1.what_am_i()

class Horse:
    def __init__(self,rider):
        self.rider = rider

class Rider:
    def __init__(self,name):
        self.name = name

Rid1 = Rider("Yutaka")
Hor1 = Horse(Rid1)
print(Hor1.rider.name)