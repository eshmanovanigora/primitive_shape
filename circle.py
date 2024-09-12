class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def getArea(self):
        """
        This method finds the area of the Circle.

        Args:
            No
        Returns:
            float or int: result.
        """
        return 3.14 * self.r ** 2

    def getLength(self):
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        return 2 * 3.14 * self.r
    
cir = Circle(1)
print(cir.getArea())
print(cir.getLength())