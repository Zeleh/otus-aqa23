from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        if not self.side_value_check(side_a, side_b)[0]:
            raise ValueError('Unacceptable value '
                             f'{self.side_value_check(side_a, side_b)[1]} '
                             'for a rectangle side. '
                             'Must be a non zero positive float')
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.name = f'Rectangle {side_a} x {side_b}'
        self.area = self.get_figure_area()
        self.perimeter = self.get_perimeter()

    def get_figure_area(self) -> float:
        self.area = self.side_a * self.side_b
        return self.area

    def get_perimeter(self) -> float:
        self.perimeter = (self.side_a + self.side_b) * 2
        return self.perimeter


class Square(Rectangle):
    def __init__(self, side_a: float):
        if not self.side_value_check(side_a)[0]:
            raise ValueError('Unacceptable value '
                             f'{self.side_value_check(side_a)[1]} '
                             'for a square side. '
                             'Must be a non zero positive float')
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = f'Square {side_a}'
        self.area = self.get_figure_area()
        self.perimeter = self.get_perimeter()

    def get_figure_area(self) -> float:
        self.area = self.side_a ** 2
        return self.area

    def get_perimeter(self) -> float:
        self.perimeter = self.side_a * 4
        return self.perimeter


rect1 = Square(2)
print(rect1.area)
print(rect1.perimeter)
rect1.side_a = 4
rect1.get_figure_area()
rect1.get_perimeter()
print(rect1.area)
print(rect1.perimeter)
