"""Тест-кейс копирования множества"""


def test_set_copy(fixture_return_set):
    copy_set = fixture_return_set.copy()
    assert copy_set == fixture_return_set
