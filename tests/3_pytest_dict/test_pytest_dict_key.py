import pytest

"""Тест-кейс на наличие ключа элемента в словаре"""


@pytest.mark.parametrize("test_input", "B")
def test_key_in_dict(test_input, fixture_return_dict):
    assert test_input in fixture_return_dict
