import pytest

"""Тест-кейс добавления элемента в конец"""


@pytest.mark.parametrize("test_input", '56')
def test_append_list(test_input, fixture_return_list):
    fixture_return_list.append(test_input)
    assert len(fixture_return_list) == 4
