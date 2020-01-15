import pytest

"""Задание строк"""


@pytest.fixture
def fixture_return_str():
    string_user = 'ython'
    return string_user


@pytest.fixture
def fixture_return_str_figures():
    string_user = '123'
    return string_user
