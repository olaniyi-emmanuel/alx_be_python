import  math
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError("You forgot to override the area() method!")

class Rectangle(Shape):
    def __init__(self, length:float, width:float):
        super().__init__()
        self.length = length
        self.width = length

    def area(self):
        return  self.length * self.width

class Circle(Shape):
    def __init__(self, radius:float):
        super().__init__()
        self.radius = radius

        def area():
            return  math.pi * (self.radius ** 2 )
