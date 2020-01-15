import pytest

"""Тест-кейс проверки сложения строк и проверка на ключевое значение python"""


@pytest.mark.parametrize("test_input", "ptb")
def test_string_1(test_input, fixture_return_str):
    print(test_input + fixture_return_str)
    assert test_input + fixture_return_str == "python"
