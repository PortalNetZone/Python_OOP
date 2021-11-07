class Square:
    def __init__(self, side=1):
        self.side = side

    def area_calculate(self):
        return pow(self.side, 2)


square = Square(5)
print(square.side, square.area_calculate())
