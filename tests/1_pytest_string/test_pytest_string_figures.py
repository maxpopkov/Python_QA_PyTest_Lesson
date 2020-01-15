"""Тест-кейс проверки, что строка состоит из цифр"""


def test_string_1(fixture_return_str_figures):
    assert fixture_return_str_figures.isdigit()
