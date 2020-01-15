"""Тест-кейс на проверку равенства множеств"""


def test_set_comparison(fixture_return_set, fixture_return_another_set):
    assert fixture_return_set == fixture_return_another_set
