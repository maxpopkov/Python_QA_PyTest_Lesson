"""Тесты для openbrewerydb"""
import pytest
import random


def test_status(api_client):
    response = api_client.get()
    assert response.ok


@pytest.mark.parametrize('by_type', ['large', 'bar'])
@pytest.mark.parametrize('by_state', ['Oklahoma', 'california'])
def test_api_filtering(api_client, by_type, by_state):
    response = api_client.get(path='/breweries', params={'by_type': by_type, 'by_state': by_state})
    assert response.json() != []
    assert response.ok


@pytest.mark.parametrize('per_page', [1, 25, 50])
def test_api_page(api_client, per_page):
    response = api_client.get(path='/breweries', params={'per_page': per_page})
    assert len(response.json()) == per_page


@pytest.mark.parametrize('single_brew_number', [random.randint(1, 50)])
def test_api_random(api_client, single_brew_number):
    response = api_client.get(path='/breweries' + '/' + str(single_brew_number))
    assert response.json()['id'] == single_brew_number


@pytest.mark.parametrize('query', ['dog', 'cat', 'bird'])
def test_api_search_query(api_client, query):
    response = api_client.get(path='/breweries/search', params={'query': query})
    assert query in response.text
