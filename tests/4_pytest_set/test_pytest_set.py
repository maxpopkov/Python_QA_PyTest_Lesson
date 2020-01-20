import pytest

"""Тест-кейс добавления элменета в множество"""


@pytest.mark.parametrize("test_input", "4")
@pytest.mark.parametrize("test_input_2", "5")
def test_set_add(test_input, test_input_2, fixture_return_set):
    fixture_return_set.add(test_input)
    fixture_return_set.add(test_input_2)
    assert len(fixture_return_set) == 5


"""Тест-кейс на проверку равенства множеств"""


def test_set_comparison(fixture_return_set, fixture_return_another_set):
    assert fixture_return_set == fixture_return_another_set


"""Тест-кейс копирования множества"""


def test_set_copy(fixture_return_set):
    copy_set = fixture_return_set.copy()
    assert copy_set == fixture_return_set


"""Тест кейс пустого множества"""


def test_value_in_set(fixture_return_set):
    assert len(fixture_return_set) > 0


"""Тест-кейс объединения множеств"""


def test_union_sets(fixture_return_set, fixture_return_another_set):
    all_set = fixture_return_set.union(fixture_return_another_set)
    assert len(all_set) == 3
