import pytest

"""Тест-кейс проверки, что символ есть в строке"""


@pytest.mark.parametrize("test_input", "th")
def test_string_1(test_input, fixture_return_str):
    assert fixture_return_str.find(test_input)
