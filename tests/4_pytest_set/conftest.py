import pytest
"""Задание множеств"""

@pytest.fixture
def fixture_return_set():
    user_set = {1, 2, 3}
    return user_set


@pytest.fixture
def fixture_return_another_set():
    user_set = {3, 2, 1}
    return user_set
