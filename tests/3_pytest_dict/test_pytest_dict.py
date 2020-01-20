import pytest

"""Тест-кейс для проверки значении словаря"""


def test_key_in_dict(fixture_return_dict):
    key_dict = fixture_return_dict.values()
    assert len(key_dict) == 3


"""Тест-кейс добавление в словарь"""


@pytest.mark.parametrize("test_input, test_input_2", ["D, E"])
def test_dict_add(test_input, test_input_2, fixture_return_dict):
    fixture_return_dict[test_input] = 4
    fixture_return_dict[test_input_2] = 5
    assert len(fixture_return_dict.values()) == 5


"""Тест-кейс копирования словаря"""


def test_copy_dict(fixture_return_dict):
    copy_dict = fixture_return_dict.copy()
    assert copy_dict == fixture_return_dict


"""Тест-кейс на наличие ключа элемента в словаре"""


@pytest.mark.parametrize("test_input", "B")
def test_key_in_dict(test_input, fixture_return_dict):
    assert test_input in fixture_return_dict


"""Тест-кейс проверки заданного значения по ключу"""


@pytest.mark.parametrize("test_input", "A")
def test_dict_get_value(test_input, fixture_return_dict):
    assert fixture_return_dict.get(test_input) == 1
