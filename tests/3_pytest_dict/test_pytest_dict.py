"""Тест-кейс для проверки значении словаря"""


def test_key_in_dict(fixture_return_dict):
    key_dict = fixture_return_dict.values()
    assert len(key_dict) == 3
