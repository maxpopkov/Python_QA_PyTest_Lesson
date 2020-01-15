"""Тест-кейс сравнения 2х списков"""


def test_comparison_lists(fixture_return_list, fixture_return_add_list):
    assert fixture_return_add_list > fixture_return_list
