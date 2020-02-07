import pytest


@pytest.fixture()
def fixture_side():
    side_figure = 30
    return side_figure


@pytest.fixture()
def fixture_height():
    triangle_h=10
    return triangle_h

@pytest.fixture()
def fixture_sides_rectangle():
    side_2 = 40
    return side_2
