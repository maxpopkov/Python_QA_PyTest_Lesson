import pytest

"""Задание списков"""


@pytest.fixture
def fixture_return_list():
    user_list = [1, 2, 3]
    return user_list


@pytest.fixture
def fixture_return_add_list():
    add_list = [4, 5, 6]
    return add_list
