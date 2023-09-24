import abc


class Figure(abc.ABC):
    def __init__(self):
        pass

    @staticmethod
    def side_value_check(*args) -> tuple:
        """function validates the data input for a figure creation.
        Returns a tuple of (True for valid data/False for invalid) and the data itself.
        Current version accepts values less than 1000000000000"""
        for i in args:
            if not isinstance(i, (int, float)) or isinstance(i, (bool, str)):
                return False, i

            if i <= 0 or i >= 1000000000000:
                return False, i

            return True, i

    @abc.abstractmethod
    def get_figure_area(self):
        """A method that defines figure's area"""
        pass

    @abc.abstractmethod
    def get_perimeter(self):
        """A method that defines figure's perimeter"""
        pass

    def sum_areas(self, figure2):
        """Adding area of a figure to current figure's area"""
        if not isinstance(figure2, Figure):
            raise ValueError('Given object is not a geometrical figure')
        return self.get_figure_area() + figure2.get_figure_area()
