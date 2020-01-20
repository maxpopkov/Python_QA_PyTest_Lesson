import pytest

"""Тест-кейс проверки, что символ есть в строке"""


@pytest.mark.parametrize("test_input, test_input_2", ["th", "om"])
def test_string_1(test_input, test_input_2, fixture_return_str):
    assert fixture_return_str.find(test_input) or fixture_return_str.find(test_input_2)


"""Тест-кейс проверки, что первый символ строки это параметр"""


@pytest.mark.parametrize("test_input", "yo")
def test_string_1(test_input, fixture_return_str):
    assert fixture_return_str[0] == test_input


"""Тест-кейс проверки, что длина строки больше 0"""


def test_string_1(fixture_return_str):
    assert len(fixture_return_str) > 0


"""Тест-кейс проверки, что строка состоит из цифр"""


def test_string_1(fixture_return_str_figures):
    assert fixture_return_str_figures.isdigit()


"""Тест-кейс проверки сложения строк и проверка на ключевое значение python"""


@pytest.mark.parametrize("test_input", "ptb")
def test_string_1(test_input, fixture_return_str):
    print(test_input + fixture_return_str)
    assert test_input + fixture_return_str == "python"
