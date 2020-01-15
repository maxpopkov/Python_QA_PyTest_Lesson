"""Тест-кейс добавление в словарь"""


def test_dict_add(fixture_return_dict):
    fixture_return_dict["D"] = 4
    assert len(fixture_return_dict.values()) == 4
