import pytest

"""Тест-кейс добавления элменета в множество"""


@pytest.mark.parametrize("test_input", "4")
def test_set_add(test_input, fixture_return_set):
    fixture_return_set.add(test_input)
    assert len(fixture_return_set) == 4
