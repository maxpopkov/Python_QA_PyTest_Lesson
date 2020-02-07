import pytest

from Lesson_05_Python.practic_figure.figure_class_subclass import *

"""
Тесты к классу "Квадрат"

"""


def test_figure_square(fixture_side):
    with pytest.raises(AttributeError):
        square = Square(length_side=fixture_side)


def test_perimeter_square(fixture_side):
    square = Square(fixture_side)
    assert square.perimeter() == 120


def test_area_square(fixture_side):
    square = Square(fixture_side)
    assert square.perimeter() == 900


def test_square_side(fixture_side):
    square = Square(fixture_side)
    assert square.length_side == 30


def test_add_area_square(fixture_side, fixture_height):
    square = Square(fixture_side)
    other_figure = Right_Triangle(fixture_side, fixture_height)
    assert square.add_square(other_figure) == 1050.0
