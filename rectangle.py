from polygon import Polygon

class Rectangle(Polygon):
    def getArea(self):
        return self.height * self.width
    def getPerimeter(self):
        return (self.height + self.width) * 2

rec1 = Rectangle(4, 6)
print(rec1.getArea())
print(rec1.getPerimeter())