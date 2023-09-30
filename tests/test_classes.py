from src.rectangle import Rectangle, Square
from src.circle import Circle
from src.triangle import Triangle
import pytest

rect_positive_test = [(1, 2, 2, 6),
                      (2.5, 4.6, 11.5, 14.2),
                      (0.001, 10, 0.01, 20.002),
                      (800, 10000, 8000000, 21600)
                      ]

"""
--------------------------------------------------------------------------------------------
                                        Positive tests
--------------------------------------------------------------------------------------------
"""


#   Rectangle

@pytest.mark.parametrize(('side_a', 'side_b', 'area', 'perimeter'), rect_positive_test)
def test_positive_rectangle(side_a, side_b, area, perimeter):
    rect1 = Rectangle(side_a, side_b)
    rect1.get_perimeter()
    rect1.get_figure_area()
    assert rect1.name == f"Rectangle {side_a} x {side_b}"
    assert rect1.area == pytest.approx(area, 0.0099)
    assert rect1.perimeter == perimeter

#   Square


@pytest.mark.parametrize(('side_a', 'area', 'perimeter'),
                         [(1, 1, 4),
                          (2.5, 6.25, 10),
                          (0.001, 0.000001, 0.004),
                          (800, 640000, 3200)])
def test_positive_square(side_a, area, perimeter):
    square1 = Square(side_a)
    square1.get_perimeter()
    square1.get_figure_area()
    assert square1.name == f'Square {side_a}'
    assert square1.area == pytest.approx(area, 0.0099)
    assert square1.perimeter == perimeter

#   Triangle


@pytest.mark.parametrize(('side_c', 'side_a', 'side_b', 'area', 'perimeter'),
                         [(3, 4, 6, 5.33, 13),
                          (10, 15, 20, 72.62, 45)])
def test_positive_triangle(side_a, side_b, side_c, area, perimeter):
    tri1 = Triangle(side_a, side_b, side_c)
    tri1.get_perimeter()
    tri1.get_figure_area()
    assert tri1.name == f'Triangle {side_a} x {side_b} x {side_c}'
    assert tri1.area == pytest.approx(area, 0.0099)
    assert tri1.perimeter == perimeter

#   Circle


@pytest.mark.parametrize(('radius', 'area', 'perimeter'),
                         [(5, 78.54, 31.42),
                          (15.7, 774.37, 98.65)])
def test_positive_circle(radius, area, perimeter):
    cir1 = Circle(radius)
    cir1.get_perimeter()
    cir1.get_figure_area()
    assert cir1.area == pytest.approx(area, 0.0099)
    assert cir1.perimeter == pytest.approx(perimeter, 0.0099)

#   Sum of areas


@pytest.mark.parametrize(('side_a', 'side_b', 'side_c', 'tri_cir'),
                         [(9.5, 2, 10, 292)])
def test_positive_sum_areas(side_a, side_b, side_c, tri_cir):
    tri1 = Triangle(side_a, side_b, side_c)
    tri1.get_figure_area()
    cir1 = Circle(side_a)
    cir1.get_figure_area()
    assert tri1.sum_areas(cir1) == pytest.approx(tri_cir, 0.0099)


"""
--------------------------------------------------------------------------------------------
                                        Negative tests
--------------------------------------------------------------------------------------------
"""
#   Rectangle


@pytest.mark.parametrize(('side_a', 'side_b', 'area', 'perimeter'),
                         [(-0.1, 4, -0.4, 7.8),
                          (0, 15, 10, 15),
                          (-4, -2, 8, -12)])
def test_negative_rectangle(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        rect = Rectangle(side_a, side_b)
        rect.get_perimeter()


@pytest.mark.parametrize(('side_a', 'side_b', 'area', 'perimeter'),
                         [(4, 8, 10, 30),
                          (10, 20, -30, 9.99)])
def test_negative_rectangle_assertion(side_a, side_b, area, perimeter):
    with pytest.raises(AssertionError):
        rect = Rectangle(side_a, side_b)
        rect.get_perimeter()
        rect.get_figure_area()
        assert rect.name == f"Rectangle {side_a} x {side_b}"
        assert rect.area == area
        assert rect.perimeter == perimeter

#   Square


@pytest.mark.parametrize(('side_a', 'area', 'perimeter'),
                         [(-1, 1, 4),
                          (0, 6.25, 10),
                          ("0.001", 0, 0.004),
                          (1000000000001, 800, 3200)])
def test_negative_square(side_a, area, perimeter):
    with pytest.raises(ValueError):
        square1 = Square(side_a)
        square1.get_perimeter()


@pytest.mark.parametrize(('side_a', 'area', 'perimeter'),
                         [(1, 4, 1),
                          (8, 32, 64),
                          (10, 40, 1000)])
def test_negative_square_assertion(side_a, area, perimeter):
    with pytest.raises(AssertionError):
        square1 = Square(side_a)
        square1.get_perimeter()
        square1.get_figure_area()
        assert square1.name == f'Square {side_a}'
        assert square1.area == pytest.approx(area, 0.0099)
        assert square1.perimeter == perimeter

#   Triangle


@pytest.mark.parametrize(('side_c', 'side_a', 'side_b', 'area', 'perimeter'),
                         [(-3, 4, 6, 5.33, 13),
                          (10, 1, 20, 72.62, 45),
                          (3, 4, True, 5.33, 13),
                          ('ABC', 4, 6, 5.33, 13)])
def test_negative_triangle(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        tri1 = Triangle(side_a, side_b, side_c)
        tri1.get_perimeter()


@pytest.mark.parametrize(('side_c', 'side_a', 'side_b', 'area', 'perimeter'),
                         [(3, 4, 6, 900, 1000),
                          (10, 15, 20, -1, 30),
                          (3, 4, 2, 1, 13),
                          (0.5, 5.6, 6, 30, 15)])
def test_negative_triangle_assertion(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(AssertionError):
        tri1 = Triangle(side_a, side_b, side_c)
        tri1.get_perimeter()
        tri1.get_figure_area()
        assert tri1.name == f'Square {side_a} x {side_b} x {side_c}'
        assert tri1.area == pytest.approx(area, 0.0099)
        assert tri1.perimeter == perimeter

#   Circle


@pytest.mark.parametrize(('radius', 'area', 'perimeter'),
                         [(-5, 78.54, 31.42),
                          (0, 774.37, 98.65)])
def test_negative_circle(radius, area, perimeter):
    with pytest.raises(ValueError):
        cir1 = Circle(radius)
        cir1.get_perimeter()


@pytest.mark.parametrize(('radius', 'area', 'perimeter'),
                         [(5, 100, 0),
                          (15.7, -1, 0.65)])
def test_negative_circle_assertion(radius, area, perimeter):
    with pytest.raises(AssertionError):
        cir1 = Circle(radius)
        cir1.get_perimeter()
        cir1.get_figure_area()
        assert cir1.area == pytest.approx(area, 0.0099)
        assert cir1.perimeter == pytest.approx(perimeter, 0.0099)

#   Sum areas


@pytest.mark.parametrize(('side_a', 'side_b', 'side_c', 'tri_cir'),
                         [(9.5, 2, 10, 292)])
def test_negative_sum_areas(side_a, side_b, side_c, tri_cir):
    with pytest.raises(ValueError):
        tri1 = Triangle(side_a, side_b, side_c)
        tri1.get_figure_area()
        cir1 = Circle(side_c)
        cir1.get_figure_area()
        assert cir1.sum_areas(1) == pytest.approx(tri_cir, 0.0099)
