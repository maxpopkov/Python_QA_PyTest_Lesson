"""Тест-кейс проверки на пустой список"""


def test_comparison_lists(fixture_return_list):
    assert len(fixture_return_list) > 0
