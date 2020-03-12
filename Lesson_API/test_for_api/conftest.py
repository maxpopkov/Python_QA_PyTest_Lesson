"""Фикстуры для коннекта, через коммандную строку"""
import pytest
import requests

url_dog_ceo = 'https://dog.ceo/api'
url_openbrewry = 'https://api.openbrewerydb.org'
url_json_placeholder = 'https://jsonplaceholder.typicode.com'


class APIClient:

    def __init__(self, address):
        self.address = address

    def get(self, path='/', params=None):
        url = self.address + path
        print("GET запрос до {}".format(url))
        return requests.get(url=url, params=params)

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.address + path
        print('POST запрос до {}'.format(url))
        return requests.post(url=url, params=params, data=data, headers=headers)


@pytest.fixture(scope='session')
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(address=base_url)


def pytest_addoption(parser):
    parser.addoption('--url',
                     action='store',
                     default='https://dog.ceo/api',
                     help='Target link for request')
