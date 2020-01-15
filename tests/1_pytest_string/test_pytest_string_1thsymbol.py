import pytest

"""Тест-кейс проверки, что первый символ строки это параметр"""


@pytest.mark.parametrize("test_input", "yo")
def test_string_1(test_input, fixture_return_str):
    assert fixture_return_str[0] == test_input
