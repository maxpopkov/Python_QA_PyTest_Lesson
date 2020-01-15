"""Тест-кейс объединения множеств"""


def test_union_sets(fixture_return_set, fixture_return_another_set):
    all_set = fixture_return_set.union(fixture_return_another_set)
    assert len(all_set) == 3
