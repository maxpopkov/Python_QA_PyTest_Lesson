"""Тест-кейс проверки, что длина строки больше 0"""


def test_string_1(fixture_return_str):
    assert len(fixture_return_str) > 0
