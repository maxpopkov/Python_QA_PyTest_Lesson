import pytest

from Lesson_05_Python.practic_figure.figure_class_subclass import *


def test_figure_circle():
    with pytest.raises(AttributeError):
        circle=Circle(circle_radius=50)

