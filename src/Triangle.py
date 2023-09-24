from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        if not self.side_value_check(side_a, side_b, side_c)[0]:
            raise ValueError('Unacceptable value '
                             f'{self.side_value_check(side_a, side_b, side_c)[1]}'
                             ' for a triangle side.\n'
                             'Must be a non zero positive float')
        if side_a + side_b <= side_c \
                or side_a + side_c <= side_b \
                or side_b + side_c <= side_a:
            raise ValueError("Couldn't create a triangle "
                             'due to the sum of two sides being lesser than '
                             'the third side\'s length')

        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f'Square {side_a} x {side_b} x {side_c}'
        self.area = self.get_figure_area()
        self.perimeter = self.get_perimeter()

    def get_perimeter(self) -> float:
        self.perimeter = self.side_a + self.side_b + self.side_c
        return self.perimeter

    def get_figure_area(self) -> float:
        p = Triangle.get_perimeter(self) / 2
        self.area = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return self.area
