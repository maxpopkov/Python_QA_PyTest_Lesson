"""Получение ссылки и кода состояние из
параметров коммандной строки."""
import requests
import pytest


def pytest_addoption(parser):
    parser.addoption('--url',
                     action='store',
                     default='https://ya.ru',
                     help="Link for checking status code")
    parser.addoption('--status_code',
                     action='store',
                     default='200',
                     help='Status code for http response')


@pytest.fixture()
def get_status_code(request):
    """Фикстура получения кода состояния из параметра ком.строки"""
    status_cmd = request.config.getoption('--status_code')
    return status_cmd


@pytest.fixture()
def get_url(request):
    """Фикстура получения ссылки из параметра ком.строки"""
    url = request.config.getoption('--url')
    api_get_url = requests.get(url)
    return api_get_url.status_code
