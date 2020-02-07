import pytest
from Lesson_05_Python.practic_figure.figure_class_subclass import *

"""
Тесты к классу "Окружность"

"""


def test_figure_circle(fixture_side):
    with pytest.raises(AttributeError):
        circle = Circle(circle_radius=fixture_side)


def test_length_circle(fixture_side):
    circle = Circle(fixture_side)
    assert circle.circle_length() == 188.4


def test_length_side(fixture_side):
    circle = Circle(fixture_side)
    assert circle.length_side == 30


def test_sqr_circle(fixture_side):
    circle = Circle(fixture_side)
    assert circle.area() == 2826.0


def test_add_area_circle(fixture_side, fixture_height):
    circle = Circle(fixture_side)
    other_figure = Right_Triangle(fixture_side, fixture_height)
    assert circle.add_square(other_figure) == 2976.0
