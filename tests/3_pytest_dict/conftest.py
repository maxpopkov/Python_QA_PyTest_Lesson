import pytest

"""Задание словаря"""


@pytest.fixture
def fixture_return_dict():
    user_dict = {"A": 1, "B": 2, "C": 3}
    return user_dict
