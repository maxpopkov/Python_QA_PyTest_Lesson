import pytest

"""Тест-кейс проверки заданного значения по ключу"""


@pytest.mark.parametrize("test_input", "A")
def test_dict_get_value(test_input, fixture_return_dict):
    assert fixture_return_dict.get(test_input) == 1
