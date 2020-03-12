"""Тест статуса кода"""

def test_catch_status(get_url, get_status_code):
    assert int(get_status_code) == get_url
