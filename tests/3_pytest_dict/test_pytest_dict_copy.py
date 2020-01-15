"""Тест-кейс копирования словаря"""


def test_copy_dict(fixture_return_dict):
    copy_dict = fixture_return_dict.copy()
    assert copy_dict == fixture_return_dict
