"""Тест кейс пустого множества"""


def test_value_in_set(fixture_return_set):
    assert len(fixture_return_set) > 0
