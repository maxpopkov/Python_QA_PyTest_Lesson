"""Тест-кейс расширения списка другим списком"""


def test_list_add(fixture_return_list, fixture_return_add_list):
    fixture_return_list.extend(fixture_return_add_list)
    assert len(fixture_return_list) == 6