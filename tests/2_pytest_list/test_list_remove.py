"""Тест-кейс удаления элемента"""


def test_del_in_list(fixture_return_list):
    del fixture_return_list[1]
    assert len(fixture_return_list) == 2
