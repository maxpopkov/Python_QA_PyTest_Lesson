import pytest

"""Тест-кейс добавления элемента в конец"""


@pytest.mark.parametrize("test_input , test_input_2", ['56', '79'])
def test_append_list(test_input, test_input_2, fixture_return_list):
    fixture_return_list.append(test_input)
    fixture_return_list.append(test_input_2)
    assert len(fixture_return_list) == 5


"""Тест-кейс расширения списка другим списком"""


def test_list_add(fixture_return_list, fixture_return_add_list):
    fixture_return_list.extend(fixture_return_add_list)
    assert len(fixture_return_list) == 6


"""Тест-кейс сравнения 2х списков"""


def test_comparison_lists(fixture_return_list, fixture_return_add_list):
    assert fixture_return_add_list > fixture_return_list


"""Тест-кейс проверки на пустой список"""


def test_comparison_lists(fixture_return_list):
    assert len(fixture_return_list) > 0


"""Тест-кейс удаления элемента"""


def test_del_in_list(fixture_return_list):
    del fixture_return_list[1]
    assert len(fixture_return_list) == 2
