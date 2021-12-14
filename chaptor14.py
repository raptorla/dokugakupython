class Square():
    square_list = []

    def __init__(self,s1):
        self.s1 = s1
        self.square_list.append(self.s1)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

squ1 = Square(5)
squ2 = Square(15)
squ3 = Square(25)

print(Square.square_list)
print(squ1)

def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "a"))