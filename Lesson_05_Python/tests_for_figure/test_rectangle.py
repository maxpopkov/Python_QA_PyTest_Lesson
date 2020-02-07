import pytest

from Lesson_05_Python.practic_figure.figure_class_subclass import *

"""
Тесты к классу "Прямоугольник"

"""


def test_figure_rectangle(fixture_side, fixture_sides_rectangle):
    with pytest.raises(AttributeError):
        rectangle = Rectangle(length_side_1=fixture_side, length_side_2=fixture_sides_rectangle)


def test_perimeter_rectangle(fixture_side, fixture_sides_rectangle):
    rectangle = Rectangle(fixture_side, fixture_sides_rectangle)
    assert rectangle.perimeter() == 140


def test_area_rectangle(fixture_side, fixture_sides_rectangle):
    rectangle = Rectangle(fixture_side, fixture_sides_rectangle)
    assert rectangle.area() == 1200


def test_rectangle_side(fixture_side, fixture_sides_rectangle):
    rectangle = Rectangle(fixture_sides_rectangle)
    assert rectangle.length_side == 30


def test_add_area_rectangle(fixture_sides_rectangle, fixture_side):
    rectangle = Rectangle(fixture_side, fixture_sides_rectangle)
    other_figure = Circle(fixture_side)
    assert rectangle.add_square(other_figure) == 4026.0
