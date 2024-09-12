from polygon import Polygon

class Square(Polygon):
    def getArea(self):
        return self.height ** 2
    def getPerimeter(self):
        return self.height * 4

sq1 = Square(4, 4)
print(sq1.getArea())
print(sq1.getPerimeter())