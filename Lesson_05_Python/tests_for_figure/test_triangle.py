import pytest

from Lesson_05_Python.practic_figure.figure_class_subclass import *

"""
Тесты к классу "Треугольник"

"""


def test_figure_triangle(fixture_side, fixture_height):
    with pytest.raises(AttributeError):
        trianfle = Right_Triangle(length_side=fixture_side, height=fixture_height)


def test_perimeter_triangle(fixture_side, fixture_height):
    triangle = Right_Triangle(fixture_side, fixture_height)
    assert triangle.perimeter() == 90


def test_area_triangle(fixture_side, fixture_height):
    triangle = Right_Triangle(fixture_side, fixture_height)
    assert triangle.area() == 150.0


def test_triangle_side(fixture_side, fixture_height):
    triangle = Right_Triangle(fixture_side, fixture_height)
    assert triangle.length_side == 30


def test_add_area_triangle(fixture_side, fixture_height):
    triangle = Right_Triangle(fixture_side, fixture_height)
    other_figure = Circle(fixture_side)
    assert triangle.add_square(other_figure) == 2976.0
