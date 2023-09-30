from src.figure import Figure


class Circle(Figure):
    pi = 3.14159

    def __init__(self, radius):
        if not self.side_value_check(radius)[0]:
            raise ValueError("Unacceptable value "
                             f"{self.side_value_check(radius)[1]}"
                             " for a circle radius. "
                             "Must be a non zero positive float")
        super().__init__()
        self.radius = radius
        self.name = f'Circle of radius {radius}'
        self.area = self.get_figure_area()
        self.perimeter = self.get_perimeter()

    def get_perimeter(self) -> float:
        self.perimeter = 2*self.pi*self.radius
        return self.perimeter

    def get_figure_area(self):
        self.area = self.pi*self.radius**2
        return self.area
